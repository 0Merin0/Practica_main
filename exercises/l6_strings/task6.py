# Write a function that removes any whitespaces
# from string `s`
def clean(s: str) -> str:
    d = s.split()
    res = "".join(d)
    return res


# Do not change the below's code
if __name__ == "__main__":
    assert clean("    c     ") == "c"
    assert clean("  d  d c ") == "ddc"
    assert clean("   ") == ""
