#!/usr/bin/env python
import unittest
import sys
sys.path.append('../lib')
import testbase
import command

class FibonacciTest(testbase.BaseTest):
    test_cases = {
            '1': '1',
            '2': '1',
            '10': '55',
            '25': '75025',
            '30': '832040',
            #'35': '9227465', #too slow for naive-recursive
            }
    def configure_command(self, test_case, base_command):
        return command.OneShotCommand(base_command).add_arg(test_case)

if __name__ == '__main__':
    unittest.main()
