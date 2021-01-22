#!/usr/bin/env python
import subprocess
import unittest
import sys
sys.path.append('../lib')
import testbase

class FibonacciTest(testbase.BaseTest):
    def configure_command_and_get_expected(self, command):
        command.append('25')
        return '75025\n'

if __name__ == '__main__':
    unittest.main()
