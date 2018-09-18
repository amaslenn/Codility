#!/usr/bin/env python
import unittest

def solution(A, B):
    fighters = []
    nfishes = len(A)

    for idx, size in enumerate(A):
        downstream = B[idx]
        if downstream:
            fighters.append(size)
            continue

        while fighters:
            f = fighters[-1]
            if f > size:
                nfishes -= 1
                break
            else:
                fighters.pop()
                nfishes -= 1

    return nfishes


class Tests(unittest.TestCase):
    """Tests for Fish solution"""
    def test_from_task(self):
        """Sample from task description"""
        self.assertEqual(2, solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]))

    def test_no_meet(self):
        """Check case where fishes don't meet"""
        self.assertEqual(2, solution([1, 2], [0, 0]))
        self.assertEqual(2, solution([1, 2], [1, 1]))

    def test_one(self):
        """Case where first/last eats others"""
        self.assertEqual(1, solution([5, 4, 3, 2, 1], [1, 0, 0, 0, 0]))

    def test_all(self):
        """Case where all alive"""
        self.assertEqual(5, solution([1, 4, 3, 2, 5], [0, 0, 0, 0, 1]))


if __name__ == '__main__':
    unittest.main(failfast=True)