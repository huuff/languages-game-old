import os
import subprocess
import unittest
import configparser
import sys
sys.path.append('.')
import command

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
        config['Commands'] = {
                'fileName': '', 
                'runCommand': '',
                'timeout': 10_000,
                }
        configVars = config['Commands']
        for root, dirs, files in os.walk(".", topdown=True):
            print(root)
            if configFile in files:
                config.read(self.build_path(root, configFile))
            if configVars['fileName'] in files:
                for test_case, expected in self.test_cases.items():
                    self.run_test(root, configVars, test_case, expected)

    def run_test(self, root, configVars, test_case, expected):
        command = [configVars['runCommand'], self.build_path(root, configVars['fileName'])]
        command = self.configure_command(test_case, command)
        try:
            actual = command.run(int(configVars['timeout']) / 1000)
            self.assertEqual(expected, self.sanitize_output(actual))
        except subprocess.TimeoutExpired:
            print('Timed out!')


    
    def configure_command(self, test_case, command): pass
