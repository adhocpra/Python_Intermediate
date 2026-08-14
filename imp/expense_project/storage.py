import csv
import json
import os

from models import Transaction


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Storage:
    FILE_JSON = os.path.join(BASE_DIR, "data.json")
    FILE_CSV = os.path.join(BASE_DIR, "data.csv")

    @staticmethod
    def save(expenses):
        data = [e.__dict__ for e in expenses]

        with open(Storage.FILE_JSON, "w") as f:
            json.dump(data, f)

        with open(Storage.FILE_CSV, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["amount", "category", "date"])
            writer.writeheader()
            writer.writerows(data)

    @staticmethod
    def load():
        try:
            with open(Storage.FILE_JSON, "r") as f:
                data = json.load(f)
                return [Transaction(**d) for d in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []


