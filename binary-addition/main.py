def to_binary(num: int) -> int:
    return bin(num).replace("0b", "")


if __name__ == "__main__":
    print(to_binary(4))
