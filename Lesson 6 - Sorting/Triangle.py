#!/usr/bin/env python
import unittest

def solution(A):
    has_triangle = 0
    if len(A) < 3:
        return has_triangle

    S = sorted(A)

    p, q, r = 0, 1, 2
    while r < len(S):
        if (S[p] + S[q] > S[r]) and (S[q] + S[r] > S[p]) and (S[r] + S[p] > S[q]):
            has_triangle = 1
            break

        p += 1
        q += 1
        r += 1

    return has_triangle


class Tests(unittest.TestCase):
    """Tests for Triangle solution"""
    def test_from_task(self):
        """Sample from task description"""
        self.assertEqual(1, solution([10, 2, 5, 1, 8, 20]))

    def test_from_task(self):
        """Sample #2 from task description"""
        self.assertEqual(0, solution([10, 50, 5, 1]))


if __name__ == '__main__':
    unittest.main(failfast=True)
