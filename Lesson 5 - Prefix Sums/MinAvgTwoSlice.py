#!/usr/bin/env python
import unittest


def solution(A):
    prefix_sums = [A[0]]
    for el in A[1:]:
        prefix_sums.append(prefix_sums[-1] + el)

    min_avg, min_index = None, 0
    for size in range(2, len(A) + 1, 1):
        for ind in range(size - 1, len(A), 1):
            slice_sum = prefix_sums[ind]
            if ind - size >= 0:
                slice_sum -= prefix_sums[ind - size]
            # print(">> size={}; min_indexd={}; s={}".format(size, ind, slice_sum))

            avg = slice_sum / size
            # print("   avg={}; min_avg={}".format(avg, min_avg))

            if min_avg is None or avg < min_avg:
                # print("   new min!")
                min_avg = avg
                min_index = ind - (size - 1)

    return min_index

class Tests(unittest.TestCase):
    """Tests for MinAvgTwoSlice solution"""
    def test_from_task(self):
        """Sample from task description"""
        self.assertEqual(1, solution([4, 2, 2, 5, 1, 5, 8]))

    def test_min1(self):
        """With negative numbers"""
        self.assertEqual(2, solution([-4, 1, 1, -10]))


if __name__ == '__main__':
    unittest.main(failfast=True)
