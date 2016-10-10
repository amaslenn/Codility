#!/usr/bin/env python
import unittest


def solution(A):
    only_pos = dict()
    for el in A:
        if el > 0:
            only_pos[el] = 1

    missing = 1
    for i in range(1, (2**8)**4 // 2):
        if i not in only_pos:
            missing = i
            break

    return missing


class Tests(unittest.TestCase):
    """Tests for MissingInteger solution"""
    def test_from_task(self):
        """Sample from task description"""
        A = [1, 3, 6, 4, 2, 1]
        self.assertEqual(5, solution(A))

    def test_all_neg(self):
        """All negative and 0"""
        A = [-1, -10, 0]
        self.assertEqual(1, solution(A))

    def test_all_pos_eq(self):
        """All positive and equal"""
        A = [1, 1, 1, 1]
        self.assertEqual(2, solution(A))

    def test_missing_max(self):
        """Missing max pos value (max input size is 100000)"""
        A = [i for i in range(1, 100000 - 1)]
        self.assertEqual(100000 - 1, solution(A))


if __name__ == '__main__':
    unittest.main()
