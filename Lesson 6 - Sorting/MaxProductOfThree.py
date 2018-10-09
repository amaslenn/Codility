#!/usr/bin/env python
import unittest

def solution(A):
    if len(A) < 3:
        return 0

    S = sorted(A)
    prod = 1
    if S[-1] > 0:
        prod = S[-3] * S[-2] * S[-1]
        if abs(sum(S[:2])) > abs(sum(S[-2:])):
            prod = S[0] * S[1] * S[-1]
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


if __name__ == '__main__':
    unittest.main(failfast=True)
