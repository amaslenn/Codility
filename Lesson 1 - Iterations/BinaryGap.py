#!/usr/bin/env python
import time
import unittest


def solution(N):
    number = str(bin(N))

    maximum, count_of_zeros = 0, 0

    # for all digits skipping 0b
    for i in range(2, len(number)):
        # get bit
        b = int(number[i])

        if b == 0x1:
            if count_of_zeros != 0:
                if count_of_zeros > maximum:
                    maximum = count_of_zeros
                count_of_zeros = 0
        else:
            count_of_zeros += 1

    return maximum

class Tests(unittest.TestCase):
    """Tests for BinaryGap solution"""
    def test_from_task_1041(self):
        """Sample from task description N=1041"""
        self.assertEqual(5, solution(1041))

    def test_from_task_9(self):
        """Sample from task description N=9"""
        self.assertEqual(2, solution(9))

    def test_from_task_529(self):
        """Sample from task description N=529"""
        self.assertEqual(4, solution(529))

    def test_from_task_15(self):
        """Sample from task description N=15"""
        self.assertEqual(0, solution(15))

    def test_zero(self):
        """Check with N=0"""
        self.assertEqual(0, solution(0))

    def test_time(self):
        """N = 2147483647, check time limit (??? sec)"""
        array = [x for x in range(100000)]
        s = time.time()
        solution(2147483647)
        e = time.time()
        self.assertLess(e-s, 0.004)


if __name__ == '__main__':
    unittest.main()
