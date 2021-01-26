import os
import subprocess
import unittest
import configparser
import sys
import glob
import copy
from . import command

config_file = 'config'

class BaseTest():
    test_class = unittest.TestCase()
    def __init__(self, root_dir):
        self.root_dir = root_dir

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
        self.recursive_descent(self.root_dir, config)

    def recursive_descent(self, root, config):
        files = glob.glob(os.path.join(root, '*'))
        config_file = os.path.join(root, 'config')
        test_file = os.path.join(root, config.get('Commands', 'file'))
        if config_file in files:
            # print(f"Reading {config_file}")
            config = copy.copy(config)
            config.read(f"{config_file}")
        for file in files:
            if os.path.isdir(file):
                print(f'Going down {file}')
                self.recursive_descent(file, config)
            if file == test_file:
                print(f"Running script at {test_file}")
                for test_case, expected in self.test_cases().items():
                    self.run_test(test_file, config, test_case, expected)



    def run_test(self, test_file, config, test_case, expected):
        command = [config.get('Commands', 'run'), test_file]
        command = self.configure_command(test_case, command)
        try:
            actual = command.run(int(config.get('Commands','timeout')) / 1000)
            self.test_class.assertEqual(expected, self.sanitize_output(actual))
        except subprocess.TimeoutExpired:
            print('Timed out!')

    def test_cases(self): # to be implemented in base class
        return {}
    
    def configure_command(self, test_case, command): # to be implemented in base class
        return command.Command()
