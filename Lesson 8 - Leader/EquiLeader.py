#!/usr/bin/env python
import unittest


def solution(A):
    # find leader for O(N)
    value, size = 0, 0
    for el in A:
        if size == 0:
            value = el
            size += 1
        else:
            if el != value:
                size -= 1
            else:
                size += 1

    if not size:
        return 0

    candidate, count = value, 0
    for el in A:
        if candidate == el:
            count += 1

    leader = -1
    if count > len(A) // 2:
        leader = candidate
    else:
        return 0

    # now look for equi leader for O(N)
    size = len(A)
    all_leaders, lleaders = count, 0
    equi_leaders = 0
    for i, el in enumerate(A[:-1]):
        if el == leader:
            lleaders += 1

        lsize, rsize = i + 1, size - i - 1
        rleaders = all_leaders - lleaders

        if lleaders > lsize // 2 and rleaders > rsize // 2:
            equi_leaders += 1

    return equi_leaders


class Tests(unittest.TestCase):
    """Tests for EquiLeader solution"""
    def test_from_task(self):
        """Sample from task description"""
        self.assertEqual(2, solution([4, 3, 4, 4, 4, 2]))

    def test_zero(self):
        """Zero equi leader"""
        self.assertEqual(0, solution([4, 3, 4]))

    def test_one(self):
        """One equi leader"""
        self.assertEqual(1, solution([1, 4, 4, 4]))


if __name__ == '__main__':
    unittest.main(failfast=True)
