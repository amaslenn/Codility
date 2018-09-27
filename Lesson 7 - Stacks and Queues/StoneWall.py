#!/usr/bin/env python
import unittest

def solution(H):
    nblocks = 0

    blocks = set()
    curr_min = H[0]
    for h in H:
        if not blocks or h >= curr_min:
            curr_min = min(curr_min, h)
            blocks.add(h)
            continue

        nblocks += len(blocks)

        blocks.clear()
        blocks.add(h)
        curr_min = h

    if blocks:
        nblocks += len(blocks)

    return nblocks


class Tests(unittest.TestCase):
    """Tests for Fish solution"""
    def test_from_task(self):
        """Sample from task description"""
        self.assertEqual(7, solution([8, 8, 5, 7, 9, 8, 7, 4, 8]))

    def test_all_same(self):
        """Same height"""
        self.assertEqual(1, solution([8, 8, 8, 8]))

    def test_all_different(self):
        """Lower and lower"""
        self.assertEqual(4, solution([8, 7, 6, 5]))


if __name__ == '__main__':
    unittest.main(failfast=True)