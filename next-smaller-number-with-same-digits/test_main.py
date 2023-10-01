import main


def test_is_greater_than():
    # assert main.is_greater_than([1, 2, 3], [1, 2, 2]) == True
    # assert main.is_greater_than([2, 2, 3], [1, 2, 2]) == True
    # assert main.is_greater_than([2, 1, 3], [2, 2, 2]) == False
    assert main.is_greater_than([7, 2, 1, 0], [2, 0, 1, 7]) == True
