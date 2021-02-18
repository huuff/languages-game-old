#!/usr/bin/env python
from ...lib.command import *
from ...lib.testcase import MultiTestCase
from main.lib.expectation import ListExpectation

def test_cases():
    return [
        MultiTestCase([['key', 'value'], 'key', '--reset'], ListExpectation(['', 'value', ''])), # put and get
        MultiTestCase(['shouldnotexist'], ListExpectation([''])), # get something that wasn't there
        MultiTestCase([['key1', 'value1'], ['key2', 'value2'], 'key1', 'key2', '--reset'], ListExpectation(['', '', 'value1', 'value2', ''])), # put and get 2
        MultiTestCase([['key', 'value1'], 'key', ['key', 'value2'], 'key', '--reset'], ListExpectation(['', 'value1', '', 'value2', ''])) # update
            ]

