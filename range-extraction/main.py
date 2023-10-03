def solution(args):
    grouped_neighbors = []
    neighbors = [args.pop(0)]
    for idx, el in enumerate(args):
        if abs(el - int(neighbors[-1])) == 1:
            neighbors.append(el)
        else:
            grouped_neighbors.append(neighbors)
            neighbors = [el]

        if idx == len(args) - 1:
            grouped_neighbors.append(neighbors)

    return ",".join(
        [
            "-".join([str(neighbors[0]), str(neighbors[-1])])
            if len(neighbors) >= 3
            else ",".join([str(neighbor) for neighbor in neighbors])
            for neighbors in grouped_neighbors
        ]
    )


if __name__ == "__main__":
    print(
        solution(
            [
                -10,
                -9,
                -8,
                -6,
                -3,
                -2,
                -1,
                0,
                1,
                3,
                4,
                5,
                7,
                8,
                9,
                10,
                11,
                14,
                15,
                17,
                18,
                19,
                20,
            ]
        )
    )
