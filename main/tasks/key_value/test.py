#!/usr/bin/env python
import sys
import os
from ...lib.command import *
from ...lib.testcase import MultiTestCase

def test_cases():
    return [
        MultiTestCase([['key', 'value'], 'key', '--reset'], ['', 'value', '']), # put and get
        MultiTestCase(['shouldnotexist'], ['']), # get something that wasn't there
        MultiTestCase([['key1', 'value1'], ['key2', 'value2'], 'key1', 'key2', '--reset'], ['', '', 'value1', 'value2', '']), # put and get 2
        MultiTestCase([['key', 'value1'], 'key', ['key', 'value2'], 'key', '--reset'], ['', 'value1', '', 'value2', '']) # update
            ]

