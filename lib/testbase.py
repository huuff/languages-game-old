import os
import subprocess
import unittest
import configparser
import sys
sys.path.append('.')
import command

config_file = 'config'

class BaseTest(unittest.TestCase):
    def build_path(self, root, file):
        return root + '/' + file

    def sanitize_output(self, output):
        if isinstance(output, str):
            return output.rstrip('\n')
        else:
            return output

    def test_template(self):
        config = configparser.ConfigParser(defaults = {
                'file': '', 
                'run': '',
                'timeout': 10_000,
                })
        config.add_section('Commands')
        for root, dirs, files in os.walk(".", topdown=True):
            print(root)
            if config_file in files:
                config.read(self.build_path(root, config_file))
            if config.get('Commands', 'file') in files:
                for test_case, expected in self.test_cases.items():
                    self.run_test(root, config, test_case, expected)

    def run_test(self, root, config, test_case, expected):
        command = [config.get('Commands', 'run'), self.build_path(root, config.get('Commands','file'))]
        command = self.configure_command(test_case, command)
        try:
            actual = command.run(int(config.get('Commands','timeout')) / 1000)
            self.assertEqual(expected, self.sanitize_output(actual))
        except subprocess.TimeoutExpired:
            print('Timed out!')


    
    def configure_command(self, test_case, command): pass
