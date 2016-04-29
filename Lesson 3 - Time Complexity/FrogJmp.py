#!/usr/bin/env python
import time
import unittest


def solution(start, finish, step):
    pass


class Tests(unittest.TestCase):
    """Tests for FrogJmp solution"""
    def test_from_task(self):
        """Sample from task description"""
        self.assertEqual(3, solution(10, 85, 30))

    def test_time(self):
        """From 1 to 1B step 1 check time limit (0.72 sec)"""
        s = time.time()
        solution(1, 1000000000, 1)
        e = time.time()
        self.assertLess(e - s, 0.72)


if __name__ == '__main__':
    unittest.main()
