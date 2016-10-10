#!/usr/bin/env python
import unittest


def solution(A):
    missing = 0

    only_pos = dict()
    for el in A:
        if el > 0:
            only_pos[el] = 1

    missing = 0
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


if __name__ == '__main__':
    unittest.main()
