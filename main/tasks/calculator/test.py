#!/usr/bin/env python
import unittest
import sys
import os
from ...lib import command
from ...lib.testcase import SimpleTestCase

def test_cases(): 
    return [
        SimpleTestCase('1 + 1', '2'),
        SimpleTestCase('5 - 2', '3'),
        SimpleTestCase('3 * 4', '12'),
        SimpleTestCase('10 + (3 * 2)', '16'),
        SimpleTestCase('10 / 3', '3'),
        SimpleTestCase('10.0 / 3.0', '3.333'),
        ]

