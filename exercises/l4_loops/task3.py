# Write two functions that calculate the factorial of `n`
#
# - `factorial_while` must use while loop;
# - `factorial_for` must use for loop.
def factorial_while(n: int) -> int:
    x = 1
    res = 1
    while n >= x:
        res *= x
        x += 1
    return res


def factorial_for(n: int) -> int:
    res = 1
    for n in range(1, n+1):
        res *= n
    return res


# Do not change the below's code
if __name__ == "__main__":
    assert factorial_while(2) == 2
    assert factorial_while(3) == 6
    assert factorial_while(4) == 24
    assert factorial_while(5) == 120
    assert factorial_while(6) == 720

    assert factorial_for(2) == 2
    assert factorial_for(3) == 6
    assert factorial_for(4) == 24
    assert factorial_for(5) == 120
    assert factorial_for(6) == 720
