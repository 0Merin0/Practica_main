def odd_str(n: int) -> str:
    s = ""
    for n in range(0, n + 1):
        if n % 2 == 1:
            s += str(n)

    # Use for loop to run from 0 to n (included)
    # and form a string `s`.
    # String `s` will contain only odd numbers from interval [0; n].
    #
    # For example,
    # (0, 1, 2, 3, 4) -> "13"
    # (0, 1, 2, 3, 4, 5, 6) -> "135"

    return s


# Do not change the below's code
if __name__ == "__main__":
    assert odd_str(4) == "13"
    assert odd_str(6) == "135"
    assert odd_str(8) == "1357"
