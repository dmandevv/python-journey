"""
001 - Two Sum

Given a list of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to `target`, as a list [i, j] with i < j.
Exactly one solution exists, and the same element can't be used twice.

    two_sum([2, 7, 11, 15], 9)  ->  [0, 1]
    two_sum([3, 2, 4], 6)       ->  [1, 2]

Run the tests:  .venv/bin/pytest challenges/001_two_sum.py
"""
import pytest

def two_sum_brute(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

def two_sum(nums: list[int], target: int) -> list[int]:
    seen_at = {}
    for i, num in enumerate(nums):
        partner = target - num
        if partner in seen_at:
            return [seen_at[partner], i]
        seen_at[num] = i

@pytest.mark.parametrize(
    "func, nums, target, expected",
    [
        pytest.param(two_sum, [2, 7, 11, 15], 9, [0, 1]),
        pytest.param(two_sum_brute, [2, 7, 11, 15], 9, [0, 1]),

        pytest.param(two_sum, [3, 2, 4], 6, [1, 2]),
        pytest.param(two_sum_brute, [3, 2, 4], 6, [1, 2]),

        pytest.param(two_sum, [3, 3], 6, [0, 1]),
        pytest.param(two_sum_brute, [3, 3], 6, [0, 1]),

        pytest.param(two_sum, [-1, -2, -3, -4, -5], -8, [2, 4]),
        pytest.param(two_sum_brute, [-1, -2, -3, -4, -5], -8, [2, 4]),
    ]
)
def test_two_sum(func, nums, target, expected):
    assert func(nums, target) == expected
