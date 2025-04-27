import json
import os

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(os.path.dirname(FILE_PATH), "data/expenses.json")


def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        try:
            data = json.load(file)
            return data if data else []
        except json.JSONDecodeError:
            return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)



