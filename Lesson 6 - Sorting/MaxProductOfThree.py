#!/usr/bin/env python
import unittest

def solution(A):
    if len(A) < 3:
        return 0

    S = sorted(A)
    prod = 1
    if S[-1] > 0:
        if S[-2] < 0:
            prod = S[0] * S[1] * S[-1]
        else:
            p1 = S[0] * S[1] * S[-1]
            p2 = S[-3] * S[-2] * S[-1]
            prod = max(p1, p2)
    else:
        for x in S[-3:]:
            prod *= x

    return prod


class Tests(unittest.TestCase):
    """Tests for MaxProductOfThree solution"""
    def test_from_task(self):
        """Sample from task description"""
        self.assertEqual(60, solution([-3, 1, 2, -2, 5, 6]))

    def test_two_nagatives(self):
        """Two negative give max"""
        self.assertEqual(12, solution([-3, -2, 1, 2]))

    def test_tricky(self):
        """Two negatives and max value give max"""
        self.assertEqual(-13*-2*6, solution([-13, -2, -1, 2, 2, 5, 6]))

    def test_all_neg(self):
        """All negative"""
        self.assertEqual(-2, solution([-13, -2, -1, -1]))

    def test_one_pos(self):
        """The only positive"""
        self.assertEqual(26, solution([-13, -2, -1, 1]))

    def test_zero(self):
        """Let's have a zero!"""
        self.assertEqual(0, solution([-13, -2, -1, 0]))

    def test_zero2(self):
        """Let's have a zero 2"""
        self.assertEqual(13*2*27, solution([-13, -2, -1, 0, 27]))


if __name__ == '__main__':
    unittest.main(failfast=True)
