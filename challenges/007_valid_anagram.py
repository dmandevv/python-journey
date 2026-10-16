"""
007 - Valid Anagram

Two words are anagrams if one uses exactly the same letters as the other,
the same number of times each, in any order. Return True if `a` and `b` are
anagrams of each other.

    is_anagram("listen", "silent")  ->  True
    is_anagram("rat", "car")        ->  False
    is_anagram("aab", "abb")        ->  False   (same letters, different counts)

Run the tests:  .venv/bin/pytest challenges/007_valid_anagram.py
"""
import pytest
from collections import Counter

def is_anagram(a: str, b: str) -> bool:
    return sorted(a) == sorted(b)

def is_anagram_count(a: str, b: str) -> bool:
    if len(a) != len(b): return False
    counts_a = {}
    counts_b = {}
    for letter in a:
        counts_a[letter] = counts_a.get(letter, 0) + 1
    for letter in b:
        counts_b[letter] = counts_b.get(letter, 0) + 1
    return counts_a == counts_b

def is_anagram_counter(a: str, b: str) -> bool:
    if len(a) != len(b): return False
    return Counter(a) == Counter(b)

@pytest.mark.parametrize("func", [is_anagram, is_anagram_count, is_anagram_counter])
@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("listen", "silent", True),
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("aab", "abb", False),        # same letters, different counts
        ("abc", "abcd", False),       # different lengths
        ("", "", True),
        ("a", "a", True),
        ("ab", "a", False),
        ("aabbcc", "ccbbaa", True),
        ("Dog", "god", False),        # case matters: "D" is not "d"
    ],
)
def test_is_anagram(func, a, b, expected):
    assert func(a, b) == expected
