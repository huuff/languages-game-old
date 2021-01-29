#!/usr/bin/env python
import sys
import os
from ...lib.command import *
from ...lib import testbase

class Test(testbase.BaseTest):
    def test_cases(self): 
        return {
            'normaltest': ['', 'normaltest', ''],
            }

    def configure_command(self, test_case, base_command):
        set_command = OneShotCommand(base_command).add_arg(test_case)
        get_command = OneShotCommand(base_command)
        reset_command = OneShotCommand(base_command).add_arg('--reset')
        return MultiCommand(base_command).add_command(set_command).add_command(get_command).add_command(reset_command)



