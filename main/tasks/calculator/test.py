#!/usr/bin/env python
from ...lib.testcase import SimpleTestCase
from ...lib.expectation import Expectation

def test_cases(): 
    return [
        SimpleTestCase('1 + 1', Expectation('2')),
        SimpleTestCase('5 - 2', Expectation('3')),
        SimpleTestCase('3 * 4', Expectation('12')),
        SimpleTestCase('10 + (3 * 2)', Expectation('16')),
        SimpleTestCase('10 / 3', Expectation('3')),
        SimpleTestCase('10.0 / 3.0', Expectation('3.333')),
        ]

