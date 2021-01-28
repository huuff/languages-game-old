#!/usr/bin/env python3
import random
import os
from ...lib import testbase
from ...lib import command

randomCase = random.sample(range(-10, 10), 20)
randomCaseExpected = randomCase.copy()
randomCaseExpected.sort()

def list_to_string(list):
    return ' '.join(map(str, list))

class Test(testbase.BaseTest):
    def test_cases(self):
        return {
                list_to_string(range(10, 0, -1)): list_to_string(range(1, 11, 1)),
                list_to_string(randomCase): list_to_string(randomCaseExpected),
                }

    def configure_command(self, test_case, baseCommand):
        return command.OneShotCommand(baseCommand).add_args(test_case)

