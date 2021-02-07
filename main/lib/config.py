import configparser
import pathlib
import copy
from .logger import *

# TODO: remove get from names

stack = []

def current():
    return stack[-1]

def update(root):
    config_file = root.joinpath('config')
    if config_file.is_file():
        with open(config_file, 'r') as f:
            config_string = '[DEFAULT]\n' + f.read() # Automatically add default section
        new_config = copy.deepcopy(current().config_parser)
        new_config.read_string(config_string)
        stack.append(Config(new_config))
    else:
        stack.append(current())

def pop():
    stack.pop()

class Config:
    def __init__(self, config_parser):
        self.config_parser = config_parser
        self.commands_config = config_parser['DEFAULT']

    def get_file(self, root):
        return root.joinpath(self.commands_config.get('file'))

    def get_timeout(self):
        return self.commands_config.getint('timeout') / 1000

    def has_pre(self):
        return self.config_parser.has_option('DEFAULT', 'pre')

    def has_post(self):
        return self.config_parser.has_option('DEFAULT', 'post')

    def get_pre(self):
        return self.commands_config.get('pre').split(' ')

    def get_run(self):
        return self.commands_config.get('run').split(' ')

    def get_post(self):
        return self.commands_config.get('post').split(' ')

    def get_logger(self):
        return Logger(Level[self.commands_config.get('log_level').upper()])

    def get_port(self):
        return self.commands_config.getint('port')
