#!/usr/bin/env python
import unittest
from math import log, floor


def solution(S, P, Q):
    array = []
    for letter in S:
        if letter == 'A':
            array.append(1)
        elif letter == 'C':
            array.append(2)
        elif letter == 'G':
            array.append(3)
        elif letter == 'T':
            array.append(4)

    N = len(array)
    # construct sparse table
    ST = [0 for i in range(0, N)]
    for i, el in enumerate(array):
        ST[i] = [0 for _ in range(0, N)]
        ST[i][0] = el
    k = 1
    while (1 << k) < N:
        for i in range(0, N - (1 << k) + 1):
            ST[i][k] = min(ST[i][k-1], ST[i + (1 << (k - 1))][k-1])
        k += 1

    # perform queries
    res = []
    for i in range(0, len(P)):
        left = P[i]
        right = Q[i]
        mid = floor(log(right - left + 1, 2))

        res.append(min(ST[left][mid], ST[right - (1 << mid) + 1][mid]))

    return res


class Tests(unittest.TestCase):
    """Tests for GenomicRangeQuery solution"""
    def test_from_task(self):
        """Sample from task description"""
        self.assertEqual([2, 4, 1], solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))


if __name__ == '__main__':
    unittest.main(failfast=True)
