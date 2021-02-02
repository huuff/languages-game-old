#!/usr/bin/env python3
import random
import os
from ...lib import command
from ...lib.testcase import ListTestCase

randomCase = random.sample(range(-10, 10), 20)
randomCaseExpected = randomCase.copy()
randomCaseExpected.sort()

def test_cases():
    return [
        ListTestCase(range(10, 0, -1), range(1, 11, 1)),
        ListTestCase(randomCase, randomCaseExpected),
            ]

