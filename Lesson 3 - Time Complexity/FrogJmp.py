#!/usr/bin/env python
import time
import unittest


def solution(start, finish, step):
    num = 0
    if finish <= start:
        return num
    if step <= 0:
        return None

    num = int((finish - start) / step)
    if start + num * step < finish:
        num += 1

    return num


class Tests(unittest.TestCase):
    """Tests for FrogJmp solution"""
    def test_from_task(self):
        """Sample from task description"""
        self.assertEqual(3, solution(10, 85, 30))

    def test_start_eq_finish(self):
        """Start == finish, step > finish"""
        self.assertEqual(0, solution(10, 10, 30))

    def test_start_eq_finish2(self):
        """Start == finish, step < finish"""
        self.assertEqual(0, solution(10, 10, 0))

    def test_start_gt_finish2(self):
        """Start > finish"""
        self.assertEqual(0, solution(20, 10, 10))

    def test_1(self):
        """1 step"""
        self.assertEqual(1, solution(1, 4, 3))

    def test_2(self):
        """2 steps"""
        self.assertEqual(2, solution(1, 7, 3))

    def test_3(self):
        """3 steps"""
        self.assertEqual(3, solution(1, 8, 3))

    def test_time(self):
        """From 1 to 1B step 1 check time limit (0.00000001 sec)"""
        s = time.time()
        res = solution(1, 1000000000, 1)
        e = time.time()
        self.assertEqual(1000000000 - 1, res)
        self.assertLess(e - s, 0.00000001)


if __name__ == '__main__':
    unittest.main()
