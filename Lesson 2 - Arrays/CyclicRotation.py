#!/usr/bin/env python
import unittest


def solution(array, shift):
    res = array
    if not res:
        return res

    for i in range(0, shift):
        res.insert(0, res.pop())
    return res


class Tests(unittest.TestCase):
    """Tests for CyclicRotation solution"""
    def test_from_task(self):
        """Sample array from task description"""
        self.assertEqual([9, 7, 6, 3, 8], solution([3, 8, 9, 7, 6], 3))

    def test_0(self):
        """Rotation 0 times"""
        self.assertEqual([3, 8, 9, 7, 6], solution([3, 8, 9, 7, 6], 0))

    def test_full(self):
        """Rotation to the size of array"""
        self.assertEqual([3, 8, 9, 7, 6], solution([3, 8, 9, 7, 6], 5))

    def test_empty(self):
        """Rotation of an empty array"""
        self.assertEqual([], solution([], 5))


if __name__ == '__main__':
    unittest.main()
