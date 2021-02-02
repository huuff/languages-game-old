#!/usr/bin/env python
import sys
import os
from ...lib.command import *
from ...lib.testcase import MultiTestCase

def test_cases():
    return [
        MultiTestCase(['normaltest', '', '--reset'], ['', 'normaltest', ''])
            ]

