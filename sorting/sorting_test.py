#!/usr/bin/env python

import os
import random
import subprocess

# TODO: Print folder name

configFile = 'config.py'

fileName=''
runCommand=''

testCase = random.sample(range(0, 10), 10)
testExpected = testCase.copy()
testExpected.sort()
testCase = list(map(str, testCase))
testCaseString = ' '.join(testCase)
testExpected = ' '.join(map(str, testExpected))

def buildPath(root, fileName):
    return root + '/' + fileName

for root, dirs, files in os.walk(".", topdown=True):
    if configFile in files:
        exec(open(buildPath(root, configFile)).read())
    if fileName in files:
        command = [runCommand, buildPath(root, fileName)]
        command.extend(testCase)
        result = subprocess.run(command, stdout=subprocess.PIPE)
        testActual = result.stdout.decode('utf-8')
        print('Tested: ' + testCaseString)
        print('Expected: ' + testExpected)
        print('Actual: ' + testActual)
        assert testExpected == testActual
