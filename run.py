#!/usr/bin/env python
import sys
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('task', type=str)
args = parser.parse_args()
task_name = args.task

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

task.Test(os.path.dirname(task.__file__)).test_template()
