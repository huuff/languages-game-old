from .config import current as config
from .logger import *

def sanitize(output):
    if isinstance(output, str):
        return output.rstrip('\n')
    elif isinstance(output, list):
        return list(map(lambda s: s.rstrip('\n'), output))
    else:
        return output

def to_string(expected):
    if isinstance(expected, list):
        return list(map(str, expected))
    else:
        return str(expected)

class Expectation():
    def __init__(self, expected):
        self.expected = to_string(expected)

    def check(self, input, actual):
        logger = config().logger()
        actual = sanitize(actual)
        try:
            assert self.expected == actual
        except AssertionError as error:
            logger.log(f'Error on input: {input}', Level.FAIL)
            logger.log(f'Expected: {self.expected}', Level.FAIL)
            logger.log(f'Got: {actual}', Level.FAIL)

class ListExpectation(Expectation):
    def check(self, input, actual):
        if not isinstance(actual, list):
            actual = actual.split()
        super().check(input, actual)
