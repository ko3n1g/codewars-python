def dir_reduc(arr):
    REDUCING_DIRS = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "WEST": "EAST",
        "EAST": "WEST",
    }

    continue_reduc = True
    intermediate_arr = arr
    while continue_reduc:
        continue_reduc = False
        reduced_arr = intermediate_arr
        intermediate_arr = []
        i = 0
        while i < len(reduced_arr):
            # First part of tuple to compare.
            el = reduced_arr[i]

            # If we’re at the last element of the list,
            # there’s no next partner to compare with.
            # So we save it and break out.
            if i == len(reduced_arr) - 1:
                intermediate_arr.append(el)
                break

            # Second part of tuple to compare.
            next_el = reduced_arr[i + 1]

            # If the tuple eliminates each other, we
            # jump the list index by two elements.
            # By eliminating two elements, we create
            # a new neighboring pair we didn’t check before.
            # Hence, the outer while loop will need another
            # iteration.
            if el == REDUCING_DIRS[next_el]:
                continue_reduc = True
                i += 2
                continue

            # If no tuple was elimated, we just jump
            # to the next position in the list and add
            # the first part to the temporary array..
            i += 1
            intermediate_arr.append(el)
    return reduced_arr


if __name__ == "__main__":
    a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]

    dir_reduc(a)
