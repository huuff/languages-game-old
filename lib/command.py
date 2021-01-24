import os
import subprocess
import time

class Command:
    def __init__(self, command):
        self.command = command

    def add_arg(self, arg):
        self.command.append(arg)
        return self

    def add_args(self, args):
        self.command.extend(args.split(' '))
        return self
    
    def run(self): pass

class OneShotCommand(Command):
    def run(self):
        output = subprocess.run(self.command, stdout=subprocess.PIPE)
        process = subprocess.Popen(self.command, stdout=subprocess.PIPE, universal_newlines=True)
        process.wait()
        return process.communicate()[0]

class LongRunningCommand(Command):
    def __init__(self, base_command, func):
        super().__init__(base_command)
        self.func = func

    def run(self):
        process = subprocess.Popen(self.command)
        time.sleep(0.1) #TODO: parameterizable

        result = self.func()

        process.terminate()
        process.wait()

        return result


        
