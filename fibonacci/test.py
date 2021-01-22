#!/usr/bin/env python
import subprocess
import unittest
import sys
sys.path.append('../lib')
import testbase


class FibonacciTest(testbase.BaseTest):
    test_cases = {
            '1': '1',
            '2': '1',
            '10': '55',
            '25': '75025',
            '30': '832040',
            #'35': '9227465', #too slow for naive-recursive
            }
    def configure_command(self, test_case, command):
        command.append(test_case) 

if __name__ == '__main__':
    unittest.main()
