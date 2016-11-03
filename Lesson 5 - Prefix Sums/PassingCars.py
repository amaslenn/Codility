#!/usr/bin/env python
import unittest


def solution(A):
    num_passing_cars, num_heading_east = 0, 0

    for el in A:
        if el == 0:
            num_heading_east += 1
        else:
            num_passing_cars += num_heading_east

    # since size of A can't be greater than 100000, following condition is always false,
    # but it mention in task
    if num_passing_cars > 1000000000:
        num_passing_cars = -1

    return num_passing_cars


class Tests(unittest.TestCase):
    """Tests for PassingCars solution"""
    def test_from_task(self):
        """Sample from task description"""
        A = [0, 1, 0, 1, 1]
        self.assertEqual(5, solution(A))

    def test_no_heading_east(self):
        """No heading east cars"""
        A = [1, 1, 1, 1, 1]
        self.assertEqual(0, solution(A))

    def test_no_heading_west(self):
        """No heading west cars"""
        A = [0, 0, 0, 0, 0]
        self.assertEqual(0, solution(A))

    # test takes ~45 sec and it mostly useless
    # def test_billion_passing_cars(self):
    #     """A billion passing cars"""
    #     A = [0] * 1000000001
    #     A.append(1)
    #     self.assertEqual(-1, solution(A))


if __name__ == '__main__':
    unittest.main()
