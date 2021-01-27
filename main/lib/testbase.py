import os
import subprocess
import unittest
import configparser
import sys
import glob
import copy
import pathlib
from . import command

config_file = 'config'

class BaseTest():
    test_class = unittest.TestCase()
    def __init__(self, root_dir):
        self.root_path = pathlib.Path(root_dir)

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
                },
                interpolation=configparser.ExtendedInterpolation())
        config.add_section('Commands')
        self.recursive_descent(self.root_path, config)

    def recursive_descent(self, root, config):
        files = list(root.glob('*'))
        config_file = root.joinpath('config')
        test_file = root.joinpath(config.get('Commands', 'file'))
        if root.joinpath('config') in files:
            config = copy.copy(config)
            config.read(config_file)
        for file in files:
            if file.is_dir():
                print(f"{file.relative_to(self.root_path.parent)}")
                self.recursive_descent(file, config)
            if file == test_file:
                for test_case, expected in self.test_cases().items():
                    self.run_test(root, config, test_case, expected)

    def run_test(self, directory, config, test_case, expected):
        command = config.get('Commands', 'run').split(' ')
        command = self.configure_command(test_case, command).set_dir(directory)
        try:
            actual = command.run(int(config.get('Commands','timeout')) / 1000)
            self.test_class.assertEqual(expected, self.sanitize_output(actual))
        except subprocess.TimeoutExpired:
            print('Timed out!')

    def test_cases(self): # to be implemented in base class
        return {}
    
    def configure_command(self, test_case, command): # to be implemented in base class
        return command.Command()
