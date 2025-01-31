# Use `for` loop to calculate the amount
# of positive number in a list of integers `n`
def count_positive(n: list[int]) -> int:
    res = 0
    for number in n:
        if number > 0:
            res += 1
    return res


# Do not change the below's code
if __name__ == "__main__":
    assert count_positive([1, 2, -3, -4]) == 2
    assert count_positive([-1, -2, -3]) == 0
    assert count_positive([4, 5, 4, 3]) == 4
