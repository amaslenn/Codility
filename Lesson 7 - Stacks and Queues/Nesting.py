#!/usr/bin/env python
import unittest

def solution(S):
    res = 1

    if not S:
        return res

    stack = [S[0]]

    for s in S[1:]:
        if s == "(":
            stack.append(s)
            continue

        # s == ")"
        if not stack:
            res = 0
            break

        stack.pop()

    if stack:
        res = 0

    return res


class Tests(unittest.TestCase):
    """Tests for Nesting solution"""
    def test_from_task(self):
        """Sample from task description"""
        self.assertEqual(1, solution("(()(())())"))

    def test_from_task2(self):
        """Sample #2 from task description"""
        self.assertEqual(0, solution("())"))

    def test_inverse(self):
        """Check )("""
        self.assertEqual(0, solution(")("))

    def test_incomplete(self):
        """Check (()"""
        self.assertEqual(0, solution("(()"))

    def test_several(self):
        """Check (())()"""
        self.assertEqual(1, solution("(())()"))

    def test_empty(self):
        """Check an empty input"""
        self.assertEqual(1, solution(""))


if __name__ == '__main__':
    unittest.main(failfast=True)
