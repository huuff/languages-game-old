#!/usr/bin/env python3
import random
import os
from ...lib import testbase
from ...lib import command
from ...lib.testcase import ListTestCase

randomCase = random.sample(range(-10, 10), 20)
randomCaseExpected = randomCase.copy()
randomCaseExpected.sort()

class Test(testbase.BaseTest):
    def test_cases(self):
        return [
            ListTestCase(range(10, 0, -1), range(1, 11, 1)),
            ListTestCase(randomCase, randomCaseExpected),
                ]

