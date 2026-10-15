"""Part 2: add and list habits."""
import storage


def add_habit(name):
    """Add a new habit. Returns False if it already exists."""
    name = name.strip().lower()
    data = storage.load()
    for habit in data["habits"]:
        if habit["name"] == name:
            return False
    data["habits"].append({"name": name, "checkins": []})
    storage.save(data)
    return True


def list_habits():
    """Return the names of all habits."""
    data = storage.load()
    return [habit["name"] for habit in data["habits"]]


if __name__ == "__main__":
    print("Added:", add_habit("gym"))
    print("Added again:", add_habit("gym"))
    print("All habits:", list_habits())
