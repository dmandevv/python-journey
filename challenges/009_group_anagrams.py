"""
009 - Group Anagrams

Put the words that are anagrams of each other into the same group, and
return the list of groups. The groups can come back in any order, and so can
the words inside each group.

    group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        ->  [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

Rule: go through the list once. No comparing every word with every other word.

Run the tests:  .venv/bin/pytest challenges/009_group_anagrams.py
"""
import pytest

def group_anagrams(words: list[str]) -> list[list[str]]:
    groups = {}
    for word in words:
        sort = "".join(sorted(word))
        groups.setdefault(sort, []).append(word)
    return list(groups.values())
    


def normalise(groups):
    """Sort the words in each group, then the groups, so any order compares equal."""
    return sorted(sorted(group) for group in groups)


@pytest.mark.parametrize(
    "words, expected",
    [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
        (["listen", "silent", "enlist", "google", "gogole"], [["listen", "silent", "enlist"], ["google", "gogole"]]),
        (["abc", "def"], [["abc"], ["def"]]),        # no anagrams: every word on its own
        (["ab", "ba", "ab"], [["ab", "ba", "ab"]]),   # duplicates are kept
        (["aab", "abb"], [["aab"], ["abb"]]),        # same letters, different counts
        (["Dog", "god"], [["Dog"], ["god"]]),        # case matters, as in 007
        (["a"], [["a"]]),
        ([""], [[""]]),
        ([], []),
    ],
)
def test_group_anagrams(words, expected):
    assert normalise(group_anagrams(words)) == normalise(expected)
