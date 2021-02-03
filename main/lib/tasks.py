import importlib

tasks = {
            "fibonacci": ".fibonacci",
            "sorting": ".sorting",
            "http-server": ".http_server",
            "calculator": ".calculator",
            "persistence": ".persistence",
        }

def import_task(task_name):
    task = importlib.import_module(tasks[task_name] + ".test", "main.tasks")
    return task
