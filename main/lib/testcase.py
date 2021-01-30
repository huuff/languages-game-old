from . import command

#TODO: Seriously DRY this

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
            for i in range(0, len(self.input)):
                curr_command = command.add_arg(self.input[i])
                actual = curr_command.run(config.get_timeout())
                actual = sanitize_output(actual)
                actuals.append(actual)
                assert self.expected[i] == actual
        except AssertionError as error:
            print(f'Error on input: {self.input}')
            print(f'Expected: {self.expected}')
            print(f'Got: {actuals} before stopping')

class FuncTestCase(TestCase):
    def run(self, command, config):
        actual = command.run(self.input, config.get_timeout())
        actual = sanitize_output(actual)
        try:
            assert self.expected == actual
        except AssertionError as error:
            print(f'Error on input: {self.input}')
            print(f'Expected: {self.expected}')
            print(f'Got: {actual}')
