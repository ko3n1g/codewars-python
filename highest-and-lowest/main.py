# LOL this is too easy


def high_and_low(numbers: str) -> str:
    list_of_digits = [int(d) for d in numbers.split(" ")]
    return f"{max(list_of_digits)} {min(list_of_digits)}"


if __name__ == "__main__":
    print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
