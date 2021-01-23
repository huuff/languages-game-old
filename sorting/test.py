#!/usr/bin/env python3
import random
import subprocess
import unittest
import sys
sys.path.append('../lib')
import testbase

randomCase = random.sample(range(-10, 10), 20)
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
