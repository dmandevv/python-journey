"""
010 - Longest Substring Without Repeating Characters

Return the length of the longest run of characters in `s` (back to back, no
gaps) where no character appears twice.

    longest_unique("abcabcbb")  ->  3   ("abc")
    longest_unique("bbbbb")     ->  1   ("b")
    longest_unique("pwwkew")    ->  3   ("wke"; "pwke" doesn't count, it skips a w)

Two versions:
    longest_unique_brute  try every starting point, and grow each one until a
                          character repeats
    longest_unique        one pass with a window that grows and shrinks,
                          nothing nested that restarts from scratch

Run the tests:  .venv/bin/pytest challenges/010_longest_unique_substring.py
"""
import pytest


def longest_unique_brute(s: str) -> int:
    longest = 0
    for starting_point in range(len(s)):
        current = set()
        for c in s[starting_point:]:
            if c in current:
                break
            current.add(c)
            if len(current) > longest:
                longest = len(current)
    return longest


def longest_unique(s: str) -> int:
    left = 0
    right = 0
    longest = 0
    window = set()
    while right < len(s):
        while s[right] in window:
            window.remove(s[left])
            left += 1
        window.add(s[right])
        right += 1
        longest = max(right - left, longest)
    return longest
        



@pytest.mark.parametrize("func", [longest_unique_brute, longest_unique])
@pytest.mark.parametrize(
    "s, expected",
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("abcdef", 6),     # nothing repeats: the whole string
        ("dvdf", 3),       # "vdf": after the second d, keep the v
        ("abba", 2),       # the second a was seen before, but outside the window
        ("tmmzuxt", 5),    # "mzuxt": same trap as "abba", further along
        ("aabbc", 2),      # every run is short: "ab" or "bc", never 3
        ("aA", 2),         # case matters
        (" ", 1),          # a space is a character too
        ("a", 1),
        ("", 0),
    ],
)
def test_longest_unique(func, s, expected):
    assert func(s) == expected
