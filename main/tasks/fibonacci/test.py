#!/usr/bin/env python
import unittest
import sys
import os
from ...lib import command
from ...lib.testcase import SimpleTestCase

def test_cases():
    return [
            SimpleTestCase('1', '1'),
            SimpleTestCase('2', '1'),
            SimpleTestCase('10', '55'),
            SimpleTestCase('25', '75025'),
            SimpleTestCase('30', '832040'),
            SimpleTestCase('35', '9227465')
            ];

