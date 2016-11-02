#!/usr/bin/env python
import unittest


def solution(N, A):
    # applied_max keeps maximum value applied after N+1 value occured
    # curr_max keeps max value accross all elements
    curr_max, applied_max = 0, 0
    max_counters = [0 for i in range(0, N)]

    for el in A:
        if el == N + 1:
            applied_max = curr_max
        else:
            max = max_counters[el-1] if max_counters[el-1] > applied_max else applied_max
            max_counters[el-1] = max + 1
            curr_max = max + 1 if max + 1 > curr_max else curr_max

    # fix untouched at all or untouched after applied_max was chahged
    for i in range(0, N):
        if max_counters[i] < applied_max:
            max_counters[i] = applied_max

    return max_counters


class Tests(unittest.TestCase):
    """Tests for MaxCounters solution"""
    def test_from_task(self):
        """Sample from task description"""
        A = [3, 4, 4, 6, 1, 4, 4]
        self.assertEqual([3, 2, 2, 4, 2], solution(5, A))

    def test_increase_only(self):
        """Only increase()"""
        A = [1, 2, 3, 4, 5]
        self.assertEqual([1, 1, 1, 1, 1], solution(5, A))

    def test_two_maxes(self):
        """Two max_counters"""
        A = [1, 6, 1, 6, 5]
        self.assertEqual([2, 2, 2, 2, 3], solution(5, A))

    def test_max_at_the_end(self):
        """Apply max_counter at the end, current max is the first element"""
        A = [1, 1, 1, 2, 6]
        self.assertEqual([3, 3, 3, 3, 3], solution(5, A))


if __name__ == '__main__':
    unittest.main()
