import os
import subprocess
import concurrent.futures
import time
import timeit
import copy
from ..lib.config import current as config
from .logger import *

executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)

class Command:
    def __init__(self, base_command, directory):
        self.command = base_command
        self.directory = directory
        self.timeout = config().get_timeout()

    def add_arg(self, arg):
        new = copy.deepcopy(self)
        if isinstance(arg, list):
            for a in list(map(str, arg)):
                new.command.append(a)
        else:
            new.command.append(arg)
        return new

    def run(self): pass

class OneShotCommand(Command):
    def run(self):
        process = subprocess.Popen(
                self.command, 
                stdout=subprocess.PIPE, 
                universal_newlines=True,
                cwd=self.directory)
        try:
            config().get_logger().log(f"Running {process.args}", Level.DEBUG)
            start = timeit.default_timer()
            process.wait(self.timeout)
            end = timeit.default_timer()
            config().get_logger().log(f"Took: {round(end-start, 5)}", Level.INFO)
        except subprocess.TimeoutExpired as err:
            process.kill()
            stdout = process.communicate()[0]
            if stdout != None:
                config().get_logger().log(stdout, Level.FAIL)
            raise err
        return process.communicate()[0]

class LongRunningCommand(Command):
    def __init__(self, base_command, root, func):
        super().__init__(base_command, root)
        self.func = func

    def run(self):
        process = subprocess.Popen(
                self.command, 
                cwd=self.directory,
                universal_newlines=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
        config().get_logger().log(f"Running {process.args}", Level.DEBUG)
        time.sleep(0.1) #TODO: parameterizable

        future = executor.submit(self.func)
        try:
            result = future.result(self.timeout)
        except concurrent.futures.TimeoutError as e:
            raise e
        finally:
            process.terminate()
            process.wait()
            config().get_logger().log(process.communicate()[1], Level.INFO)

        return str(result)

def get_pre(root):
    return OneShotCommand(config().get_pre(), root)

def get_post(root):
    return OneShotCommand(config().get_post(), root)
