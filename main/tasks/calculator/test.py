#!/usr/bin/env python
import unittest
import sys
import os
from ...lib import testbase, command

class Test(testbase.BaseTest):
    def test_cases(self): 
        return {
            '1 + 1': '2',
            '5 - 2': '3',
            '3 * 4': '12',
            '10 + (3 * 2)': '16',
            '10 / 3': '3',
            '10.0 / 3.0' : '3.333'
            }

    def configure_command(self, test_case, base_command):
        return command.OneShotCommand(base_command).add_arg(test_case)

