import subprocess
import pathlib
import types
from . import command
from . import config
from . import testcase
from .logger import *
from concurrent.futures import TimeoutError

class BaseTest():
    def __init__(self, root_dir, test_cases, default_config):
        self.test_cases = test_cases
        self.root_path = pathlib.Path(root_dir)
        self.default_config = default_config

    def sanitize_output(self, output):
        if isinstance(output, str):
            return output.rstrip('\n')
        else:
            return output

    def start(self):
        self.recursive_descent(self.root_path, self.default_config)

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
                for test_case in self.test_cases:
                    self.run_test(root, config, test_case)
                if config.has_post():
                    config.get_post(root).run(config.get_timeout())

    def run_test(self, directory, config, test_case):
        try:
            test_case.run(config.get_run(), directory, config)
        except (subprocess.TimeoutExpired, TimeoutError):
            config.get_logger().log('Timed out!', Level.FAIL)
