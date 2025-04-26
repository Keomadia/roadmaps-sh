import json
import os

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(os.path.dirname(FILE_PATH), "tasks.json")


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        try:
            data = json.load(file)
            return data if data else []
        except json.JSONDecodeError:
            return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)
