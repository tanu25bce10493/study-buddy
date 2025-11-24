import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "db.json")

def load_data():
    if not os.path.exists(DB_PATH):
        return {"subjects": {}, "tasks": [], "quiz_results": []}

    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
