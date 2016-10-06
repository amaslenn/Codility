#!/usr/bin/env python
import unittest


def solution(A):
    result = 0
    same = dict()
    has_same = False

    for i in range(0, len(A)):
        result += i + 1
        result -= A[i]
        if A[i] in same:
            has_same = True
            break
        else:
            same[A[i]] = 1

    return 1 if not result and not has_same else 0


class Tests(unittest.TestCase):
    """Tests for TapeEquilibrium solution"""
    def test_from_task(self):
        """Sample from task description"""
        A = [4, 1, 3, 2]
        self.assertEqual(1, solution(A))

    def test_from_task2(self):
        """Sample #2 from task description"""
        A = [4, 1, 3]
        self.assertEqual(0, solution(A))

    def test_empty(self):
        """Empty input"""
        A = []
        self.assertEqual(1, solution(A))

    def test_missing_first(self):
        """Missing 1"""
        A = [2, 3, 4]
        self.assertEqual(0, solution(A))

    def test_missing_last(self):
        """Missing last"""
        A = [2, 4, 1]
        self.assertEqual(0, solution(A))

    def test_missing_last(self):
        """Case from evaluation"""
        A = [1, 4, 1]
        self.assertEqual(0, solution(A))


if __name__ == '__main__':
    unittest.main()
