import importlib
import re

tasks = {
            "fibonacci": ".fibonacci",
            "sorting": ".sorting",
            "http-server": ".http_server",
            "calculator": ".calculator",
            "persistence": ".persistence",
        }

def import_tasks(task_name):
    if (task_name == "all"):
        regex = re.compile(r".*")
    else:
        regex = re.compile(rf".*{task_name}.*")

    matching_tasks = []
    for name, module in tasks.items():
        if regex.fullmatch(name):
            task = importlib.import_module(module + ".test", "main.tasks")
            matching_tasks.append(task)
    return matching_tasks
