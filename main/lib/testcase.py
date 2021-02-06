from .command import OneShotCommand, LongRunningCommand
from .logger import *
import subprocess
from .config import current as config

def sanitize_output(output):
    if isinstance(output, str):
        return output.rstrip('\n')
    else:
        return output

def assert_equals(input, expected, actual):
    logger = config().get_logger()
    try:
        assert expected == actual
    except AssertionError as error:
        logger.log(f'Error on input: {input}', Level.FAIL)
        logger.log(f'Expected: {expected}', Level.FAIL)
        logger.log(f'Got: {actual}', Level.FAIL)

def run_with_timeout(command):
    try:
        return command.run(config().get_timeout())
    except (subprocess.TimeoutExpired, TimeoutError):
        return "TIMED OUT"

class TestCase:
    def __init__(self, input, expected):
        self.input = input
        self.expected = expected

class SimpleTestCase(TestCase):
    def __init__(self, input, expected):
        if isinstance(expected, list):
            expected = ' '.join(list(map(str, expected)))
        super().__init__(input, expected)

    def run(self, base_command, root):
        command = OneShotCommand(base_command, root).add_arg(self.input)
        actual = run_with_timeout(command)
        actual = sanitize_output(actual)
        assert_equals(self.input, self.expected, actual)

class MultiTestCase(TestCase):
    def run(self, base_command, root):
        command = OneShotCommand(base_command, root)
        actuals = [] 
        for i in range(0, len(self.input)):
            cur_command = command.add_arg(self.input[i])
            actual = run_with_timeout(cur_command)
            actual = sanitize_output(actual)
            actuals.append(actual)
        assert_equals(self.input, self.expected, actuals)

class FuncTestCase(TestCase):
    def run(self, base_command, root):
        command = LongRunningCommand(base_command, root, self.input)
        actual = run_with_timeout(command)
        actual = sanitize_output(actual)
        assert_equals(self.input, self.expected, actual)
