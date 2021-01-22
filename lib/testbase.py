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
                command = [configVars['runCommand'], self.buildPath(root, configVars['fileName'])]
                expected = self.configure_command_and_get_expected(command)
                result = subprocess.run(command, stdout=subprocess.PIPE)
                testActual = result.stdout.decode('utf-8')
                self.assertEqual(expected, testActual)
    
    def configure_command_and_get_expected(self, command): pass
