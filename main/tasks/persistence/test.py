#!/usr/bin/env python
import sys
import os
from ...lib.command import *
from ...lib import testbase
from ...lib.testcase import MultiTestCase

class Test(testbase.BaseTest):
    def test_cases(self):
        return [
            MultiTestCase(['normaltest', '', '--reset'], ['', 'normaltest', ''])
                ]

    def configure_command(self, base_command):
        return OneShotCommand(base_command)



