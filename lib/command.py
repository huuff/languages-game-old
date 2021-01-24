import os
import subprocess
import concurrent.futures
import time
import timeit

executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
class Command:
    def __init__(self, base_command):
        self.command = base_command

    def add_arg(self, arg):
        self.command.append(arg)
        return self

    def add_args(self, args):
        self.command.extend(args.split(' '))
        return self
    
    def run(self): pass

class OneShotCommand(Command):
    def run(self, timeout):
        process = subprocess.Popen(self.command, stdout=subprocess.PIPE, universal_newlines=True)
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
        process = subprocess.Popen(self.command)
        time.sleep(0.1) #TODO: parameterizable

        future = executor.submit(self.func)
        result = future.result(timeout)

        process.terminate()
        process.wait()

        return result


        
