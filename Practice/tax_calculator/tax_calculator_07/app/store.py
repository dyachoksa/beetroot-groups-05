import json

from .models import Income

# Each income will be an instance of a class Income
incomes = []


def load_incomes(filename="store.json"):
    global incomes

    try:
        with open(filename, "r") as f:
            incomes = list(map(Income.from_dict, json.load(f)))
        
        if not incomes:
            incomes = []
    except FileNotFoundError:
        print(f"Warning: {filename} does not exist. It will be created automatically with your first income.")


def save_incomes(filename="store.json"):
    with open(filename, "w") as f:
        json.dump(list(map(lambda x: x.to_dict(), incomes)), f, indent=2)
