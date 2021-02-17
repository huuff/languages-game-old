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
        config.update(root)
        current_config = config.current()
        files = list(root.glob('*'))
        for file in files:
            if file.is_dir():
                print(f"{file.relative_to(self.root_path.parent)}")
                self.recursive_descent(file)
            if file == current_config.file(root):
                if current_config.has_pre():
                    command.get_pre(root).run()
                for test_case in self.test_cases:
                    test_case.run(current_config.run(), root)
                if current_config.has_post():
                    command.get_post(root).run()
        config.pop()
