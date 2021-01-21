#!/usr/bin/env python
import os
import random
import subprocess
import unittest
import configparser

# TODO: Print folder name

configFile = 'config'

def buildPath(root, fileName):
    return root + '/' + fileName

class SortingTest(unittest.TestCase):
    def test_sort(self):
        config = configparser.ConfigParser()
        config['Commands'] = {'fileName': '', 'runCommand': ''}
        configVars = config['Commands']
        for root, dirs, files in os.walk(".", topdown=True):
            if configFile in files:
                config.read(buildPath(root, configFile))
            if configVars['fileName'] in files:
                command = [configVars['runCommand'], buildPath(root, configVars['fileName'])]
                command.append('25')
                result = subprocess.run(command, stdout=subprocess.PIPE)
                testActual = result.stdout.decode('utf-8')
                self.assertEqual('75025\n', testActual)

if __name__ == '__main__':
    unittest.main()
