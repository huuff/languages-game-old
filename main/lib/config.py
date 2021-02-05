import configparser
import pathlib
import copy
from .logger import *

# TODO: remove get from names
# TODO: maybe automatically add default when reading

stack = []

def current():
    return stack[-1]

class Config:
    def __init__(self, config_parser):
        self.config_parser = config_parser
        self.commands_config = config_parser['Commands']

    def get_file(self, root):
        return root.joinpath(self.commands_config.get('file'))

    def get_timeout(self):
        return self.commands_config.getint('timeout') / 1000

    def has_pre(self):
        return self.config_parser.has_option('Commands', 'pre')

    def has_post(self):
        return self.config_parser.has_option('Commands', 'post')

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

    def get_updated(self, root):
        config_file = root.joinpath('config')
        if config_file.is_file():
            new_config = copy.deepcopy(self.config_parser)
            new_config.read(config_file)
            return Config(new_config)
        else:
            return self
