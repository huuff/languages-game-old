#!/usr/bin/env python
import random
import subprocess
import unittest
import sys
sys.path.append('../lib')
import testbase

# TODO: Accept newline at end of output?

testCase = random.sample(range(0, 10), 10)
testExpected = testCase.copy()
testExpected.sort()
testCase = list(map(str, testCase))
testCaseString = ' '.join(testCase)
testExpected = ' '.join(map(str, testExpected))

class SortingTest(testbase.BaseTest):
    def configure_command_and_get_expected(self, command):
        command.extend(testCase)
        return testExpected


if __name__ == '__main__':
    unittest.main()
