#!/usr/bin/env python
import unittest


def solution(A):
    result, part_sum = 0, 0
    for el in A:
        part_sum = max(0, part_sum + el)
        result = max(part_sum, result)

    if result == 0:
        result = max(A)

    return result


class Tests(unittest.TestCase):
    """Tests for MaxSliceSum solution"""
    def test_from_task(self):
        """Sample from task description"""
        self.assertEqual(5, solution([3, 2, -6, 4, 0]))

    def test_negative(self):
        """All negative numbers"""
        self.assertEqual(-2, solution([-3, -2, -6, -4]))


if __name__ == '__main__':
    unittest.main(failfast=True)
