#!/usr/bin/env python
import time
import unittest


def solution(array):
    odd = set()
    for x in array:
        if x in odd:
            odd.remove(x)
        else:
            odd.add(x)

    return odd.pop()


class Tests(unittest.TestCase):
    """Tests for OddOccurrencesInArray solution"""
    def test_from_task(self):
        """Sample array from task description"""
        self.assertEqual(7, solution([9, 3, 9, 3, 9, 7, 9]))


if __name__ == '__main__':
    unittest.main()
