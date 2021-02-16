from .command import OneShotCommand, LongRunningCommand
from .logger import *
import subprocess
from .config import current as config
from .expectation import *

def run_with_timeout(command):
    try:
        return command.run()
    except (subprocess.TimeoutExpired, TimeoutError):
        return "TIMED OUT"

class TestCase:
    def __init__(self, input, expected):
        self.input = input
        if isinstance(expected, list):
            self.expected = ListExpectation(expected)
        else:
            self.expected = Expectation(expected)

class SimpleTestCase(TestCase):
    def run(self, base_command, root):
        command = OneShotCommand(base_command, root).add_arg(self.input)
        actual = run_with_timeout(command)
        self.expected.check(self.input, actual)

class MultiTestCase(TestCase):
    def run(self, base_command, root):
        command = OneShotCommand(base_command, root)
        actuals = [] 
        for i in range(0, len(self.input)):
            cur_command = command.add_arg(self.input[i])
            actual = run_with_timeout(cur_command)
            actuals.append(actual)
        self.expected.check(self.input, actuals)

class FuncTestCase(TestCase):
    def run(self, base_command, root):
        command = LongRunningCommand(base_command, root, self.input)
        actual = run_with_timeout(command)
        self.expected.check(self.input, actual)
