#!/usr/bin/env python
import sys
import os
import argparse
import configparser
from pathlib import Path
from main.lib import testbase
from main.lib.config import Config
from main.lib.tasks import import_tasks


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('task', type=str, help='Name of the task to be run')
    parser.add_argument('-l', '--level', nargs='?', type=str, help='Level of logging')
    parser.add_argument('-t', '--timeout', nargs='?', type=int, help='Maximum test running time')
    return parser.parse_args()

def create_default_config(args):
    default_configparser = configparser.ConfigParser(defaults = {
            'file': '', 
            'run': '',
            'timeout': args.timeout if args.timeout != None else 10_000 ,
            'log_level': args.level if args.level != None else 'info',
            },
            interpolation=configparser.ExtendedInterpolation())
    default_configparser.add_section('Commands')
    return Config(default_configparser)

args = parse_arguments()
default_config = create_default_config(args)
tasks = import_tasks(args.task)

for task in tasks:
    testbase.BaseTest(os.path.dirname(task.__file__), \
            task.test_cases(), \
            default_config) \
            .start()
