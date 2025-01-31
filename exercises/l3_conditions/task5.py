# Write the body of the function to make the script work without errors
def is_vowel(c: str) -> bool:
    if c in ["a", "e", "o", "i", "u", "A", "E", "O", "I", "U"]:
        return True
    else:
        return False


if __name__ == "__main__":
    # Do not change the below asserts
    assert is_vowel("a") is True
    assert is_vowel("e") is True
    assert is_vowel("z") is False
    assert is_vowel("B") is False
