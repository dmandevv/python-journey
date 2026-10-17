"""
008 - Best Time to Buy and Sell Stock

`prices[i]` is the price of a stock on day i. Buy on one day and sell on a
LATER day. Return the most profit you can make, or 0 if no trade makes money.

    max_profit([7, 1, 5, 3, 6, 4])  ->  5   (buy at 1 on day 1, sell at 6 on day 4)
    max_profit([7, 6, 4, 3, 1])     ->  0   (the price only falls, so don't trade)

Two versions:
    max_profit_brute  try every buy day with every later sell day
    max_profit        one pass through the list, nothing nested

Run the tests:  .venv/bin/pytest challenges/008_best_time_to_buy_and_sell.py
"""
import pytest


def max_profit_brute(prices: list[int]) -> int:
    most_profit = 0
    for buy_day in range(0, len(prices)):
        for sell_day in range(buy_day + 1, len(prices)):
            if (profit := prices[sell_day] - prices[buy_day]) > most_profit:
                most_profit = profit
    return most_profit


def max_profit(prices: list[int]) -> int:
    best_day_to_buy = 0
    best_profit = 0
    for today in range(1, len(prices)):
        if (profit := prices[today] - prices[best_day_to_buy]) > best_profit:
            best_profit = profit
        if prices[today] < prices[best_day_to_buy]:
            best_day_to_buy = today
    return best_profit


@pytest.mark.parametrize("func", [max_profit_brute, max_profit])
@pytest.mark.parametrize(
    "prices, expected",
    [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),           # only falls: no trade
        ([1, 2], 1),
        ([2, 1], 0),                    # can't sell before you buy
        ([5], 0),                       # one day: nothing to sell on
        ([], 0),
        ([3, 3, 3], 0),                 # flat: no profit
        ([2, 4, 1], 2),                 # the lowest price comes too late to use
        ([3, 8, 1, 4], 5),              # buying at the lowest price isn't always best
        ([1, 2, 4, 2, 5, 7, 2, 4, 9, 0], 8),
    ],
)
def test_max_profit(func, prices, expected):
    assert func(prices) == expected
