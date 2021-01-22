#!/usr/bin/env python
import subprocess
import unittest
import sys
sys.path.append('../lib')
import testbase


class FibonacciTest(testbase.BaseTest):
    test_cases = {
            '1': '1\n',
            '2': '1\n',
            '10': '55\n',
            '25': '75025\n',
            '30': '832040\n',
            '35': '9227465\n',
            }
    def configure_command(self, test_case, command):
        command.append(test_case) 

if __name__ == '__main__':
    unittest.main()
