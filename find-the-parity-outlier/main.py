def find_outlier(integers):
    evens = [d for d in integers if d % 2 == 0]
    odds = [d for d in integers if d % 2 == 1]

    return odds[0] if len(evens) > len(odds) else evens[0]
