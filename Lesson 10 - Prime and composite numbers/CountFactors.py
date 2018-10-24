#!/usr/bin/env python
import unittest


def solution(N):
    factors = 0

    i = 1
    while i * i < N:
        if N % i == 0:
            factors += 2
        i += 1

    if N % (i * i) == 0:
        factors += 1

    return factors


class Tests(unittest.TestCase):
    """Tests for CountFactors solution"""
    def test_from_task(self):
        """Sample from task description"""
        self.assertEqual(8, solution(24))

    def test_one(self):
        """Count for 1"""
        self.assertEqual(1, solution(1))


if __name__ == '__main__':
    unittest.main(failfast=True)
