import math
from copy import copy
from dataclasses import dataclass
from decimal import Decimal, getcontext
from typing import List

getcontext().prec = 200


@dataclass
class Fraction:
    nominator: int
    denominator: int

    @property
    def decimal(self):
        return Decimal(self.nominator) / Decimal(self.denominator)

    @classmethod
    def from_decimal(cls, decimal: float) -> "Fraction":
        target_digit = [Decimal(d) for d in str(decimal).split(".")]
        nominator = decimal * 10 ** len(str(target_digit[1]))
        denominator = 10 ** len(str(target_digit[1]))

        return cls(nominator=nominator, denominator=denominator)

    def __repr__(self) -> str:
        nominator = self.nominator
        denominator = self.denominator

        if nominator == 0:
            return "0"

        if nominator / denominator < 1:
            denominator /= nominator
            nominator = 1
            return f"{nominator}/{denominator}"
        else:
            return f"{int(nominator / denominator)}"

    def __sub__(self, other: "Fraction") -> "Fraction":
        left = copy(self)
        right = copy(other)

        left.nominator *= right.denominator
        left.denominator *= right.denominator
        right.nominator *= self.denominator
        right.denominator *= self.denominator
        return Fraction(
            nominator=left.nominator - right.nominator, denominator=right.denominator
        )

    def __ge__(self, other) -> bool:
        return self.decimal >= other


def decompose(n: str) -> List[str]:
    """This will be fun!
    It smells like an recursive problem in which we each call stack
    tries to subtract the greatest possible fraction and let’s the
    next call stack figure out the rest.
    Let’s see if this sticks :P

    With floating point round errors, it’s best not to use division
    but rather subtraction. Thus, we need a different data structure
    with allows us to handle nominator and denominator separately.
    """

    if "/" in n:
        target_digit = [int(d) for d in n.split("/")]
        target_digit = Fraction(
            nominator=Decimal(target_digit[0]), denominator=Decimal(target_digit[1])
        )
    elif "." in n:
        target_digit = Fraction.from_decimal(Decimal(n))
    else:
        target_digit = Fraction(nominator=Decimal(int(n)), denominator=1)

    # For zero or natural numbers we can directly return
    if float(int(target_digit.decimal)) == float(target_digit.decimal):
        return [str(int(target_digit.decimal))] if target_digit.decimal > 0 else []

    decompositions: List[Fraction] = []

    # If we have digit greater than 1, our first component will be greater than one as well.
    # Precisely, it will be the greatest natural number smaller or equal to our target digit.
    # Otherwise, the component shall be at 1/2 or smaller (denominator just one digit greater
    # than the target_digit’s one).
    if target_digit.decimal > 1:
        nominator = int(target_digit.decimal)
        denominator = 1

    else:
        nominator = 1
        denominator = max(2, math.floor(1 / target_digit.decimal))

    component = Fraction(
        nominator=Decimal(nominator),
        denominator=Decimal(denominator),
    )

    while target_digit.decimal > 0:
        if (remainder := target_digit - component) >= 0:
            target_digit = remainder
            decompositions.append(component)
            if target_digit.nominator > 0:
                denominator = max(2, math.floor(1 / target_digit.decimal)) - 1

        denominator += 1
        component = Fraction(
            nominator=Decimal(1),
            denominator=Decimal(denominator),
        )

    return [str(d) for d in decompositions]
