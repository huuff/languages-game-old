#!/usr/bin/env python
import sys
import os
import argparse
import configparser
from pathlib import Path
from main.lib import testbase
from main.lib.config import Config


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

def import_task(task_name):
    if task_name == 'fibonacci' or task_name == 'fib':
        import main.tasks.fibonacci.test as task
    elif task_name == 'sorting' or task_name == 'sort':
        import main.tasks.sorting.test as task
    elif task_name == 'http-server' or task_name == 'server':
        import main.tasks.http_server.test as task
    elif task_name == 'calculator' or task_name == 'calc':
        import main.tasks.calculator.test as task
    elif task_name == 'persistence' or task_name == 'persist':
        import main.tasks.persistence.test as task
    else:
        import main.tasks.fibonacci as task # TODO: better default for when task is missing
    return task

args = parse_arguments()
default_config = create_default_config(args)
task = import_task(args.task)

testbase.BaseTest(os.path.dirname(task.__file__), \
        task.test_cases(), \
        default_config) \
        .start()
