#!/usr/bin/env python
import unittest


def solution(A):
    size = len(A)

    # do verifications
    if not size:
        return None
    if size < 2:
        return A[0]

    # calc result for P=1
    P = 1
    sum_left = A[0]
    sum_right = sum(A[2:])
    result = abs(sum_left - sum_right)

    # walk through whole array to find minumal difference
    for P in range(2, size - 2):
        sum_left = sum(A[0:(P-1)])
        sum_right = sum(A[(P+1):(size-1)])
        diff = abs(sum_left - sum_right)
        if diff < result:
            result = diff

    return result


class Tests(unittest.TestCase):
    """Tests for TapeEquilibrium solution"""
    def test_from_task(self):
        """Sample array from task description"""
        self.assertEqual(1, solution([3,1,2,4,3]))

    def test_from_task_negative(self):
        """Sample array from task description but using negative numbers"""
        self.assertEqual(1, solution([-3,-1,-2,-4,-3]))

    def test_two_elements(self):
        """Array of two elements"""
        self.assertEqual(3, solution([3,3]))

    def test_zero_elements(self):
        """Array with five 0's"""
        self.assertEqual(0, solution([0,0,0,0,0]))

    def test_empty(self):
        """Empty array"""
        self.assertEqual(None, solution([]))

    def test_one_element(self):
        """Array with single element"""
        self.assertEqual(69, solution([69]))


if __name__ == '__main__':
    unittest.main()
