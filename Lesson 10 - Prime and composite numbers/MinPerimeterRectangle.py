#!/usr/bin/env python
import unittest


def solution(N):
    perimetr, a = N << 3, 1
    while a * a <= N:
        if N % a == 0:
            b = N // a
            perimetr = min(perimetr, 2 * (a + b))
        a += 1

    return perimetr


class Tests(unittest.TestCase):
    """Tests for MinPerimeterRectangle solution"""
    def test_from_task(self):
        """Sample from task description"""
        self.assertEqual(22, solution(30))

    def test_two(self):
        """Area is 2"""
        self.assertEqual(6, solution(2))

    def test_prime(self):
        """Area is a prime"""
        self.assertEqual(24, solution(11))

    def test_1(self):
        """Area is 1"""
        self.assertEqual(4, solution(1))

    def test_36(self):
        """Area is 36"""
        self.assertEqual(24, solution(36))


if __name__ == '__main__':
    unittest.main(failfast=True)
