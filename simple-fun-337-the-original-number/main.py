NUMBERS = {
    "ONE": "1",
    "TWO": "2",
    "THREE": "3",
    "FOUR": "4",
    "FIVE": "5",
    "SIX": "6",
    "SEVEN": "7",
    "EIGHT": "8",
    "NINE": "9",
    "ZERO": "0",
}

import collections


def get_distinct_numbers(numbers: set):
    """For each character in the alphabet, we want to store the numbers
    containing such an character. Characters with a single number only are
    giving hint to the numbers we want to start with.

    We use an argument instead of the gobal NUMBERS set since we will be
    eliminating numbers while scanning through the encrypted sequence.
    """
    distinct_numbers = collections.defaultdict(list)
    for number in numbers:
        for char in number:
            distinct_numbers[char].append(number)

    return distinct_numbers


def original_number(s: str) -> str:
    """Most intuitively, we can probe for each word the existence in `s`,
    and each char occurs we assume it was in the original number. That
    might as well be a good approach given that each word is unique in its
    chars.
    Let’s see and hope for the best :P

    The strategy worked, but it wasn’t clear that digits might repeat.
    That means that we need to consume the input string while reducing it
    after finding matches until it is empty.

    Nevermind, it doesn’t work very good. My initial worries about detecting
    false positives has become true since some numbers have overlapping chars.
    But not all, i.e. SIX cannot be confused with others.
    """

    original_numbers = []
    numbers = NUMBERS
    while len(s):
        distinct_numbers = get_distinct_numbers(numbers).items()

        if not len(distinct_numbers):
            break
        numbers_to_scan = min(distinct_numbers, key=lambda v: len(v[1]))[1]

        if not len(numbers_to_scan):
            continue
        number = numbers_to_scan.pop(0)

        continue_eliminate = True
        while continue_eliminate:
            continue_eliminate = False
            if all(char in s for char in number):
                original_numbers.append(NUMBERS[number])
                for char in number:
                    s = s.replace(char, "", 1)
                continue_eliminate = True

        del numbers[number]

    return "".join(number for number in sorted(original_numbers))


if __name__ == "__main__":
    print(original_number("ONETWO"))
