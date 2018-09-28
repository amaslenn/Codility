#!/usr/bin/env python
import unittest

def solution(H):
    nblocks, blocks = 0, []
    for h in H:
        if not blocks or h >= blocks[-1]:
            blocks.append(h)
            continue

        b = blocks[-1]
        tmp = set()
        while b > h:
            tmp.add(b)
            blocks.pop()
            if not blocks:
                break
            b = blocks[-1]

        blocks.append(h)
        nblocks += len(tmp)

    tmp = set(blocks)
    nblocks += len(tmp)

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

    def test_all_different(self):
        """Saw"""
        self.assertEqual(3, solution([1, 2, 1, 2]))


if __name__ == '__main__':
    unittest.main(failfast=True)