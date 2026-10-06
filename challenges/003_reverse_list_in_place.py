"""
003 - Reverse a List In Place

Reverse `items` in place: change the list you were given, don't build a new
one. Return nothing (None), the same way `list.sort()` does.

Rules: no `items.reverse()`, no `reversed()`, no slicing (`items[::-1]`).
Use two pointers, one at each end, moving toward each other.

    nums = [1, 2, 3, 4]
    reverse_in_place(nums)
    nums  ->  [4, 3, 2, 1]

Run the tests:  .venv/bin/pytest challenges/003_reverse_list_in_place.py
"""
import pytest


def reverse_in_place(items: list) -> None:
    if len(items) <= 1:
        return None
    p1 = 0
    p2 = len(items) - 1
    while(p1 < p2):
        items[p1], items[p2] = items[p2], items[p1]
        p1 += 1
        p2 -= 1
    



@pytest.mark.parametrize(
    "items, expected",
    [
        ([1, 2, 3, 4], [4, 3, 2, 1]),       # even length
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]), # odd length: the middle stays put
        ([], []),
        (["a"], ["a"]),
        ([1, 2], [2, 1]),
        ([7, 7, 1], [1, 7, 7]),
        (["x", 0, None], [None, 0, "x"]),
    ],
)
def test_reverse_in_place(items, expected):
    assert reverse_in_place(items) is None
    assert items == expected


def test_changes_the_same_list_object():
    items = [1, 2, 3]
    same = items
    reverse_in_place(items)
    assert same is items
    assert same == [3, 2, 1]
