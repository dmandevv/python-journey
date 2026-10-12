"""
006 - Binary Search

`nums` is sorted from smallest to largest, with no duplicates. Return the
index of `target`, or -1 if it isn't there.

Rules: no `in`, no `.index()`, and don't check every item one by one.
Each step must halve the part of the list that could still hold the answer.

    search([-1, 0, 3, 5, 9, 12, 15], 9)  ->  4
    search([-1, 0, 3, 5, 9, 12, 15], 2)  ->  -1

Run the tests:  .venv/bin/pytest challenges/006_binary_search.py
"""
import pytest


def search(nums: list[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    while(low <= high):
        mid = (low + high) // 2
        mid_num = nums[mid]
        if mid_num == target:
            return mid
        if target < mid_num:
            high = mid - 1
        else:
            low = mid + 1
    return -1


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        ([-1, 0, 3, 5, 9, 12], -1, 0),    # first item
        ([-1, 0, 3, 5, 9, 12], 12, 5),    # last item
        ([5], 5, 0),
        ([5], 3, -1),
        ([], 1, -1),                      # empty list
        ([1, 3], 3, 1),                   # two items: easy to get stuck in a loop here
        ([1, 3, 5, 7, 9], 0, -1),         # smaller than everything
        ([1, 3, 5, 7, 9], 10, -1),        # bigger than everything
    ],
)
def test_search(nums, target, expected):
    assert search(nums, target) == expected


def test_large_list():
    nums = list(range(0, 2_000_000, 2))   # a million even numbers
    assert search(nums, 1_234_568) == 617_284
    assert search(nums, 1_234_567) == -1
