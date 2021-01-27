#!/usr/bin/env python
import unittest
import sys
import os
from ...lib import testbase, command

class Test(testbase.BaseTest):
    def test_cases(self): 
        return {
            '1': '1',
            '2': '1',
            '10': '55',
            '25': '75025',
            '30': '832040',
            '35': '9227465', #too slow for naive-recursive
            }

    def __init__(self):
        super().__init__(os.path.dirname(__file__))

    def configure_command(self, test_case, base_command):
        return command.OneShotCommand(base_command).add_arg(test_case)

