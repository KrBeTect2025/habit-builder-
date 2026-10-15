"""Part 1: storage.

Habits live in a JSON file so they survive after the program closes.
Shape of the data:
    {"habits": [{"name": "gym", "checkins": ["2026-10-15"]}]}
"""
import json
from pathlib import Path

DATA_FILE = Path("habits.json")


def load():
    """Read habits from disk. Return an empty structure if no file yet."""
    if not DATA_FILE.exists():
        return {"habits": []}
    with DATA_FILE.open() as f:
        return json.load(f)


def save(data):
    """Write habits to disk."""
    with DATA_FILE.open("w") as f:
        json.dump(data, f, indent=2)
