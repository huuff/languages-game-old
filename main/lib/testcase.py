from .command import OneShotCommand, LongRunningCommand

def sanitize_output(output):
    if isinstance(output, str):
        return output.rstrip('\n')
    else:
        return output

def assert_equals(input, expected, actual):
    try:
        assert expected == actual
    except AssertionError as error:
        print(f'Error on input: {input}')
        print(f'Expected: {expected}')
        print(f'Got: {actual}')


class TestCase:
    def __init__(self, input, expected):
        self.input = input
        self.expected = expected

class SimpleTestCase(TestCase):
    def run(self, base_command, root, config):
        command = OneShotCommand(base_command, config).set_dir(root).add_arg(self.input)
        actual = command.run(config.get_timeout())
        actual = sanitize_output(actual)
        assert_equals(self.input, self.expected, actual)

# TODO: maybe ditch this one
class ListTestCase(TestCase):
    def __init__(self, input, expected):
        super().__init__(list(map(str, input)), ' '.join(list(map(str, expected))))

    def run(self, base_command, root, config):
        command = OneShotCommand(base_command, config).set_dir(root)
        for arg in self.input:
            command = command.add_arg(arg)
        actual = command.run(config.get_timeout())
        actual = sanitize_output(actual)
        assert_equals(self.input, self.expected, actual)

class MultiTestCase(TestCase):
    def run(self, base_command, root, config):
        command = OneShotCommand(base_command, config).set_dir(root)
        actuals = [] 
        for i in range(0, len(self.input)):
            curr_command = command.add_arg(self.input[i])
            actual = curr_command.run(config.get_timeout())
            actual = sanitize_output(actual)
            actuals.append(actual)
        assert_equals(self.input, self.expected, actuals)

class FuncTestCase(TestCase):
    def run(self, base_command, root, config):
        command = LongRunningCommand(base_command, config).set_dir(root)
        actual = command.run(self.input, config.get_timeout())
        actual = sanitize_output(actual)
        assert_equals(self.input, self.expected, actual)
