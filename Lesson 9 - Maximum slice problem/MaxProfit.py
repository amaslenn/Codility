#!/usr/bin/env python
import unittest


def solution(A):
    profit = 0
    if not A:
        return profit

    buy_price = A[0]
    for sell_price in A[1:]:
        if sell_price - buy_price < 0:
            buy_price = sell_price

        profit = max(profit, sell_price - buy_price)

    return profit


class Tests(unittest.TestCase):
    """Tests for MaxProfit solution"""
    def test_from_task(self):
        """Sample from task description"""
        self.assertEqual(356, solution([23171, 21011, 21123, 21366, 21013, 21367]))

    def test_no_profit(self):
        """No profit"""
        self.assertEqual(0, solution([23171, 23011, 22123, 21366, 21013, 20367]))

    def test_mine(self):
        """Up and down"""
        self.assertEqual(5, solution([10, 9, 12, 7, 6, 11]))


if __name__ == '__main__':
    unittest.main(failfast=True)
