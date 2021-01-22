#!/usr/bin/env python
import random
import subprocess
import unittest
import sys
sys.path.append('../lib')
import testbase

# TODO: Accept newline at end of output?

randomCase = random.sample(range(-100, 100), 100)
randomCaseExpected = randomCase.copy()
randomCaseExpected.sort()

def list_to_string(list):
    return ' '.join(map(str, list))

class SortingTest(testbase.BaseTest):
    test_cases = {
            list_to_string(range(10, 0, -1)): list_to_string(range(1, 11, 1)),
            list_to_string(randomCase): list_to_string(randomCaseExpected),
            }

    def configure_command(self, test_case, command):
        command.extend(test_case.split(' '))



if __name__ == '__main__':
    unittest.main()
