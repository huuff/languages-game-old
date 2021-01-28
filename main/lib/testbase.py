import subprocess
import unittest
import pathlib
from . import command
from . import config

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
        self.recursive_descent(self.root_path, config.default())

    def recursive_descent(self, root, config):
        config = config.get_updated(root)
        files = list(root.glob('*'))
        for file in files:
            if file.is_dir():
                print(f"{file.relative_to(self.root_path.parent)}")
                self.recursive_descent(file, config)
            if file == config.get_file(root):
                if config.has_pre():
                    config.get_pre(root).run(config.get_timeout())
                for test_case, expected in self.test_cases().items():
                    self.run_test(root, config, test_case, expected)
                if config.has_post():
                    config.get_post(root).run(config.get_timeout())

    def run_test(self, directory, config, test_case, expected):
        command = self.configure_command(test_case, config.get_run()).set_dir(directory)
        try:
            actual = command.run(config.get_timeout())
            self.test_class.assertEqual(expected, self.sanitize_output(actual))
        except subprocess.TimeoutExpired:
            print('Timed out!')
        except AssertionError as error:
            args_array = error.args[0].split('\n')
            print(f'Error on input: {test_case}')
            print(f'Expected: {args_array[1][2:]}')
            print(f'Got: {args_array[2][2:]}')

    def test_cases(self): # to be implemented in base class
        return {}
    
    def configure_command(self, test_case, command): # to be implemented in base class
        return command.Command()
