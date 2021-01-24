import os
import subprocess
import unittest
import configparser
import sys
sys.path.append('.')
import command
# TODO: Print folder name

configFile = 'config'

class BaseTest(unittest.TestCase):
    def build_path(self, root, fileName):
        return root + '/' + fileName

    def sanitize_output(self, output):
        if isinstance(output, str):
            return output.rstrip('\n')
        else:
            return output

    def test_template(self):
        config = configparser.ConfigParser()
        config['Commands'] = {'fileName': '', 'runCommand': ''}
        configVars = config['Commands']
        for root, dirs, files in os.walk(".", topdown=True):
            if configFile in files:
                config.read(self.build_path(root, configFile))
            if configVars['fileName'] in files:
                for test_case, expected in self.test_cases.items():
                    command = [configVars['runCommand'], self.build_path(root, configVars['fileName'])]
                    command = self.configure_command(test_case, command)
                    actual = command.run()
                    self.assertEqual(expected, self.sanitize_output(actual))
    
    def configure_command(self, test_case, command): pass
