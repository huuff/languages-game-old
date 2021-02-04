#!/usr/bin/env python3
import random
import os
from ...lib import command
from ...lib.testcase import SimpleTestCase

randomCase = random.sample(range(-10, 10), 20)
randomCaseExpected = randomCase.copy()
randomCaseExpected.sort()

def test_cases():
    return [
        SimpleTestCase(list(range(10, 0, -1)), list(range(1, 11, 1))),
        SimpleTestCase(list(randomCase), list(randomCaseExpected)),
            ]

