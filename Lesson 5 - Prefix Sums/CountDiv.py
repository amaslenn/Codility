#!/usr/bin/env python
import unittest


def solution(A, B, K):
    res = 0
    if B > 0:
        res = B // K
    if A > 0:
        res -= A // K
        if A % K == 0:  # keep left bound value
            res += 1
    else:
        res += 1    # 0 is mod for everyone

    return res


class Tests(unittest.TestCase):
    """Tests for CountDiv solution"""
    def test_from_task(self):
        """Sample from task description"""
        self.assertEqual(3, solution(6, 11, 2))

    def test_empty_range(self):
        """Empty range"""
        self.assertEqual(0, solution(11, 11, 2))

    def test_only_min(self):
        """Only min is divisible"""
        self.assertEqual(1, solution(11, 12, 11))

    def test_only_max(self):
        """Only max is divisible"""
        self.assertEqual(1, solution(11, 12, 12))

    def test_only_min_max(self):
        """Both min and max are divisible, range is empty"""
        self.assertEqual(1, solution(12, 12, 12))

    def test_min_max(self):
        """Both min and max are divisible, range is not empty"""
        self.assertEqual(4, solution(6, 12, 2))

    def test_fail1(self):
        """Data from failing case after 1st submit"""
        self.assertEqual(20, solution(11, 345, 17))

    def test_zero(self):
        """Zero is mod for anyone"""
        self.assertEqual(1, solution(0, 0, 7))

    def test_fail2(self):
        """Data from failing case after 2d submit"""
        self.assertEqual(8, solution(0, 14, 2))


if __name__ == '__main__':
    unittest.main(failfast=True)
