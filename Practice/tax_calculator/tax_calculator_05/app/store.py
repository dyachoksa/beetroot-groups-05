import json

# Each income in format: {"year": 2023, "month": 9, "amount": 200}
incomes = []


def load_incomes(filename="store.json"):
    global incomes

    try:
        with open(filename, "r") as f:
            incomes = json.load(f)

            # or
            # data = f.read()
            # incomes = json.loads(data)
        
        if not incomes:
            incomes = []
    except FileNotFoundError:
        print(f"Warning: {filename} does not exist. It will be created automatically with your first income.")


def save_incomes(filename="store.json"):
    with open(filename, "w") as f:
        json.dump(incomes, f, indent=2)

        # or
        # data = json.dumps(incomes)
        # f.write(data)
