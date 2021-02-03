import os
import subprocess
import concurrent.futures
import time
import timeit
import copy
from .logger import *

executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
class Command:
    def __init__(self, base_command, config):
        self.command = base_command # TODO: is base_command necessary here? testbase could pass it
        self.directory = ""
        self.config = config

    def add_arg(self, arg):
        new = copy.deepcopy(self)
        new.command.append(arg)
        return new

    def set_dir(self, directory): # TODO: remove it
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
            self.config.get_logger().log(f"Running {process.args}", Level.DEBUG)
            start = timeit.default_timer()
            process.wait(timeout)
            end = timeit.default_timer()
            self.config.get_logger().log(f"Took: {round(end-start, 5)}", Level.INFO)
        except subprocess.TimeoutExpired as err:
            process.kill()
            print(process.communicate()[0])
            raise err
        return process.communicate()[0]

class LongRunningCommand(Command):
    def run(self, func, timeout):
        process = subprocess.Popen(self.command, cwd=self.directory)
        self.config.get_logger().log(f"Running {process.args}", Level.DEBUG)
        time.sleep(0.1) #TODO: parameterizable

        future = executor.submit(func)
        try:
            result = future.result(timeout)
        except concurrent.futures.TimeoutError as e:
            raise e
        finally:
            process.terminate()
            process.wait()

        return result
