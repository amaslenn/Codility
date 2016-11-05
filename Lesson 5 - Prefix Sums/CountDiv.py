#!/usr/bin/env python
import unittest


def solution(A, B, K):
    res = (B - A) // K

    if A % K == 0:
        res += 1
    if A + res * K < B and B % K == 0:
        res += 1

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


if __name__ == '__main__':
    unittest.main()
