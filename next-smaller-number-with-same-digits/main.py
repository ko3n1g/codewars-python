###############################################################################
# Problem description:
#
# Write a function that takes a positive integer # and returns the next smaller
# positive integer containing the same digits.
#
# For example:
# ```python
# nextSmaller(21) == 12
# nextSmaller(531) == 513
# nextSmaller(2071) == 2017
# ```

import functools
import itertools
import sys
import timeit


def main(inp: int) -> int:
    digits = tuple(d for d in str(inp))
    solution = ["0"]
    for item in itertools.permutations(tuple(sorted(digits)), len(digits)):
        if digits == item:
            break
        solution = item

    return -1 if solution[0] == "0" else int("".join([str(c) for c in solution]))


if __name__ == "__main__":
    inp = sys.argv[1]
    timed_func = functools.partial(main, inp)
    print(timeit.Timer(timed_func).timeit(10))
    print(main(inp))
