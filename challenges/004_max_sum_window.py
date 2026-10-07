"""
004 - Maximum Sum of k Consecutive Numbers

Given a list of integers `nums` and a window size `k`, return the largest sum
of any k numbers that sit next to each other in the list.
You can assume 1 <= k <= len(nums).

    max_window_sum([2, 1, 5, 1, 3, 2], 3)  ->  9     (5 + 1 + 3)
    max_window_sum([2, 3, 4, 1, 5], 2)     ->  7     (3 + 4)

Run the tests:  .venv/bin/pytest challenges/004_max_sum_window.py
"""
import pytest


def max_window_sum(nums: list[int], k: int) -> int:
    max_sum = float("-inf")
    for i in range(0, len(nums) - k + 1):      
        window = nums[i:i+k]
        if (s := sum(window)) > max_sum:
            max_sum = s
    return max_sum

def max_sliding_window_sum(nums: list[int], k: int) -> int:
    max_sum = sum(nums[0:k])
    current_window = max_sum
    for i in range(1, len(nums) - k + 1):      
        current_window += nums[i+k-1] - nums[i-1]
        max_sum = max(current_window, max_sum)
    return max_sum

@pytest.mark.parametrize("func", [max_window_sum, max_sliding_window_sum])
@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([2, 1, 5, 1, 3, 2], 3, 9),
        ([2, 3, 4, 1, 5], 2, 7),
        ([4, 2, 1], 1, 4),             # k = 1: just the biggest number
        ([4, 2, 1], 3, 7),             # k = len: the whole list
        ([-1, -2, -3, -4], 2, -3),     # all negative: the answer is negative, not 0
        ([1, 1, 1, 10], 2, 11),        # best window is at the very end
        ([5, -10, 6, 1, -2, 7], 3, 6), # 6 + 1 - 2 = 5 or 1 - 2 + 7 = 6
    ],
)
def test_max_window_sum(func, nums, k, expected):
    assert func(nums, k) == expected
