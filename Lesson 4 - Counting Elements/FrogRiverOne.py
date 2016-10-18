#!/usr/bin/env python
import unittest

MAX_VALUE = 200000


def solution(X, A):
    if not A:
        return -1

    steps = [MAX_VALUE for i in range(0, X)]
    for i, pos in enumerate(A):
        if pos <= X and steps[pos - 1] > i:
            steps[pos - 1] = i

    time = -1
    for s in steps:
        if s == MAX_VALUE:
            time = -1
            break
        if s > time:
            time = s

    return time


class Tests(unittest.TestCase):
    """Tests for FrogRiverOne solution"""
    def test_from_task(self):
        """Sample from task description"""
        A = [1, 3, 1, 4, 2, 3, 5, 4]
        self.assertEqual(6, solution(5, A))

    def test_empty(self):
        """Empty input array"""
        self.assertEqual(-1, solution(1, []))

    def test_no_way(self):
        """No way with only start point"""
        self.assertEqual(-1, solution(5, [1, 1, 1]))

    def test_no_way2(self):
        """No way with only end points"""
        self.assertEqual(-1, solution(5, [6, 6, 6]))

    def test_start_eq_finish(self):
        """Finish on first step"""
        self.assertEqual(0, solution(1, [1, 6, 6]))


if __name__ == '__main__':
    unittest.main()
