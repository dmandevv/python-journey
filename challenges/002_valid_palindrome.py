"""
002 - Valid Palindrome

A phrase is a palindrome if it reads the same forwards and backwards once
you ignore case and keep only letters and digits.

Return True if `s` is a palindrome, otherwise False.

    is_palindrome("A man, a plan, a canal: Panama")  ->  True
    is_palindrome("race a car")                      ->  False
    is_palindrome(" ")                               ->  True   (nothing left is still a palindrome)
Run the tests:  .venv/bin/pytest challenges/002_valid_palindrome.py
"""
import pytest


def is_palindrome(s: str) -> bool:
    s_rev = s[::-1]
    s_clean = s_rev_clean = ""
    for _, c in enumerate(s):
        if c.isalnum():
            s_clean += c.lower()
    for _, c in enumerate(s_rev):
        if c.isalnum():
            s_rev_clean += c.lower()
    return s_clean == s_rev_clean

def is_palindrome_efficient(s: str) -> bool:
    p1 = 0
    p2 = len(s) - 1
    while p1 < p2:
        while p1 < p2 and not s[p1].isalnum():
            p1 += 1
        while p1 < p2 and not s[p2].isalnum():
            p2 -= 1
        if s[p1].lower() != s[p2].lower():
            return False
        p1 += 1
        p2 -= 1
    return True


@pytest.mark.parametrize("func", [is_palindrome, is_palindrome_efficient])
@pytest.mark.parametrize(
    "s, expected",
    [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("", True),
        ("a", True),
        ("ab", False),
        ("No 'x' in Nixon", True),
        ("0P", False),          # digits count, and "0" isn't "p"
        ("12321", True),
    ],
)
def test_is_palindrome(func, s, expected):
    assert func(s) == expected
