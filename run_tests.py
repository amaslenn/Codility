#!/usr/bin/env python
import argparse
from os import listdir
from subprocess import run, PIPE
import os.path

parser = argparse.ArgumentParser(description='Run tests for all lessons')
parser.add_argument('-v', dest='verbose', action='store_true', default=False, help='verbose mode')
args = parser.parse_args()

root_content = listdir('.')
tests = list()
for f in root_content:
    if f.startswith('.'):
        continue

    if not os.path.isdir(f):
        continue

    dir_content = listdir(f)
    for item in dir_content:
        if item.endswith('.py'):
            py = os.path.join(f, item)
            tests.append(py)

err = 0
for script in tests:
    ret = run(['python', script], stdout=PIPE, stderr=PIPE, universal_newlines=True)

    if ret.returncode or args.verbose:
        err += ret.returncode
        print('Tests for "{}" exited with {}.'.format(script, ret.returncode))
        print('STDOUT: {}'.format(ret.stdout))
        print('STDERR: {}'.format(ret.stderr))

with open("README.md", "r") as f:
    tests_in_readme = set()
    for line in f:
        if "Lesson" in line and "%" in line:
            test = line.split()[2]
            tests_in_readme.add(test)

    real_tests = set()
    for t in tests:
        name = os.path.splitext(os.path.basename(t))[0]
        real_tests.add(name)


    sym_diff = real_tests ^ tests_in_readme
    if sym_diff:
        print("Tests not added to README:", real_tests - tests_in_readme)
        print("Non existing tests in README:", tests_in_readme - real_tests)
        err += 1

exit(err)
