#!/usr/bin/env python
import time
import unittest
import random


def solution(A):
    exp, real = 1, 0

    for i in range(0, len(A)):
        exp += i + 2
        real += A[i]

    missing = exp - real

    return missing


class Tests(unittest.TestCase):
    """Tests for PermMissingElem solution"""
    def test_from_task(self):
        """Sample from task description"""
        A = [2, 3, 1, 5]
        self.assertEqual(4, solution(A))

    def test_empty(self):
        """Empty array"""
        self.assertEqual(1, solution([]))

    def test_single(self):
        """Single element array"""
        self.assertEqual(1, solution([2]))

    def test_single2(self):
        """Single element array #2"""
        self.assertEqual(2, solution([1]))

    def test_double(self):
        """Double element array"""
        self.assertEqual(2, solution([1, 3]))

    def test_missing_first(self):
        """Custom example with missing first"""
        A = [2, 3, 4, 5]
        self.assertEqual(1, solution(A))

    def test_missing_last(self):
        """Custom example with missing last"""
        A = [2, 3, 4, 1]
        self.assertEqual(5, solution(A))


if __name__ == '__main__':
    unittest.main()
