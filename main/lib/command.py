import os
import subprocess
import concurrent.futures
import time
import timeit
import copy


executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
class Command:
    def __init__(self, base_command):
        self.command = base_command # TODO: is base_command necessary here? testbase could pass it
        self.directory = ""

    def add_arg(self, arg):
        new = copy.deepcopy(self)
        new.command.append(arg)
        return new

    def add_args(self, args):
        new = copy.deepcopy(self)
        new.command.extend(args.split(' '))
        return new

    def set_dir(self, directory):
        new = copy.deepcopy(self)
        new.directory = directory
        return new
    
    def run(self): pass

class OneShotCommand(Command):
    def run(self, timeout):
        process = subprocess.Popen(
                self.command, 
                stdout=subprocess.PIPE, 
                universal_newlines=True,
                cwd=self.directory)
        try:
            start = timeit.default_timer()
            process.wait(timeout)
            end = timeit.default_timer()
            print("Took: ", round(end - start, 5))
        except subprocess.TimeoutExpired as err:
            process.kill()
            print(process.communicate()[0])
            raise err
        return process.communicate()[0]

class LongRunningCommand(Command):
    def __init__(self, base_command, func):
        super().__init__(base_command)
        self.func = func

    def run(self, timeout):
        process = subprocess.Popen(self.command, cwd=self.directory)
        time.sleep(0.1) #TODO: parameterizable

        future = executor.submit(self.func)
        result = future.result(timeout)

        process.terminate()
        process.wait()

        return result

class MultiCommand(Command):
    def __init__(self, base_command):
        super().__init__(base_command)
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)
        return self

    # TODO: timeout for all commands maybe
    def run(self, timeout):
        result = []
        for command in self.commands: # TODO: too dirty
            result.append(command.set_dir(self.directory).run(timeout))
        return result
