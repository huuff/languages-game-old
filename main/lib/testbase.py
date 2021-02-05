import subprocess
import pathlib
import types
from . import command
from . import config
from . import testcase
from .logger import *
from concurrent.futures import TimeoutError

class BaseTest():
    def __init__(self, root_dir, test_cases):
        self.test_cases = test_cases
        self.root_path = pathlib.Path(root_dir)

    def sanitize_output(self, output):
        if isinstance(output, str):
            return output.rstrip('\n')
        else:
            return output

    def start(self):
        self.recursive_descent(self.root_path)

    def recursive_descent(self, root):
        config.stack.append(config.current().get_updated(root))
        files = list(root.glob('*'))
        for file in files:
            if file.is_dir():
                print(f"{file.relative_to(self.root_path.parent)}")
                self.recursive_descent(file)
            if file == config.current().get_file(root):
                if config.current().has_pre():
                    command.get_pre(root).run(config.current().get_timeout())
                for test_case in self.test_cases:
                    test_case.run(config.current().get_run(), root)
                if config.current().has_post():
                    command.get_post(root).run(config.current().get_timeout())
        config.stack.pop()
