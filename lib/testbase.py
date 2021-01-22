import os
import subprocess
import unittest
import configparser
# TODO: Print folder name

configFile = 'config'


class BaseTest(unittest.TestCase):
    def buildPath(self, root, fileName):
        return root + '/' + fileName

    def test_template(self):
        config = configparser.ConfigParser()
        config['Commands'] = {'fileName': '', 'runCommand': ''}
        configVars = config['Commands']
        for root, dirs, files in os.walk(".", topdown=True):
            if configFile in files:
                config.read(self.buildPath(root, configFile))
            if configVars['fileName'] in files:
                for test_case, expected in self.test_cases.items():
                    command = [configVars['runCommand'], self.buildPath(root, configVars['fileName'])]
                    self.configure_command(test_case, command)
                    result = subprocess.run(command, stdout=subprocess.PIPE)
                    print(result.args) # for debugging
                    testActual = result.stdout.decode('utf-8')
                    self.assertEqual(expected, testActual.rstrip('\n'))
    
    def configure_command(self, test_case, command): pass
