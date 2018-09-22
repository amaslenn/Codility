#!/usr/bin/env python
import unittest

def solution(S):
    res = 1
    stack = []

    for s in S:
        if s in ["(", "[", "{"]:
            stack.append(s)
            continue

        if not stack:
            res = 0
            break

        if s == ")" and stack[-1] == "(":
            stack.pop()
        elif s == "]" and stack[-1] == "[":
            stack.pop()
        elif s == "}" and stack[-1] == "{":
            stack.pop()
        else:
            res = 0
            break

    if stack:
        res = 0

    return res


class Tests(unittest.TestCase):
    """Tests for Brackets solution"""
    def test_from_task(self):
        """Sample from task description"""
        self.assertEqual(1, solution("{[()()]}"))

    def test_from_task_neg(self):
        """Sample #2 from task description"""
        self.assertEqual(0, solution("([)()]"))

    def test_only_open(self):
        """Only open"""
        self.assertEqual(0, solution("([{"))

    def test_only_close(self):
        """Only close"""
        self.assertEqual(0, solution(")]}"))


if __name__ == '__main__':
    unittest.main(failfast=True)
