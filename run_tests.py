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

exit(err)
