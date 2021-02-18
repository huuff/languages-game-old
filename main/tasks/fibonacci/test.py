#!/usr/bin/env python
from ...lib.testcase import SimpleTestCase
from ...lib.expectation import Expectation

def test_cases():
    return [
            SimpleTestCase('1', Expectation('1')),
            SimpleTestCase('2', Expectation('1')),
            SimpleTestCase('10', Expectation('55')),
            SimpleTestCase('25', Expectation('75025')),
            SimpleTestCase('30', Expectation('832040')),
            SimpleTestCase('35', Expectation('9227465'))
            ];

