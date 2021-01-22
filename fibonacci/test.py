#!/usr/bin/env python
import os
import subprocess
import unittest
import configparser
import sys
sys.path.append('../lib')
import testbase
# TODO: Print folder name

class FibonacciTest(testbase.BaseTest):
    def configure_command_and_get_expected(self, command):
        command.append('25')
        return '75025\n'

if __name__ == '__main__':
    unittest.main()
