from . import command

def sanitize_output(output):
    if isinstance(output, str):
        return output.rstrip('\n')
    else:
        return output

class TestCase:
    def __init__(self, input, expected):
        self.input = input
        self.expected = expected

class SimpleTestCase(TestCase):
    def run(self, command, config):
        command = command.add_arg(self.input)
        actual = command.run(config.get_timeout())
        actual = sanitize_output(actual)
        try:
            assert self.expected == actual
        except AssertionError as error:
            print(f'Error on input: {self.input}')
            print(f'Expected: {self.expected}')
            print(f'Got: {actual}')

# TODO: maybe ditch this one
class ListTestCase(TestCase):
    def run(self, command, config):
        command = command.add_args(self.input)
        actual = command.run(config.get_timeout())
        actual = sanitize_output(actual)
        try:
            assert self.expected == actual
        except AssertionError as error:
            print(f'Error on input: {self.input}')
            print(f'Expected: {self.expected}')
            print(f'Got: {actual}')

class MultiTestCase(TestCase):
    def run(self, command, config):
        actuals = [] # TODO: maybe tidy this up a little
        try:
            for i in self.input:
                curr_command = command.add_arg(i)
                actual = curr_command.run(config.get_timeout())
                actual = sanitize_output(actual)
                assert self.expected == actual
        except AssertionError as error:
            print(f'Error on input: {self.input}')
            print(f'Expected: {self.expected}')
            print(f'Got: {actuals} before stopping')
