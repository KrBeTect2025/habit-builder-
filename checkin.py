"""Part 3: daily check-in."""
from datetime import date

import storage


def check_in(name, day=None):
    """Mark a habit as done for a day (default: today).

    Returns "done" on success, "already" if it was already marked,
    and "missing" if the habit does not exist.
    """
    name = name.strip().lower()
    day = day or date.today().isoformat()  # e.g. "2026-10-15"
    data = storage.load()
    for habit in data["habits"]:
        if habit["name"] == name:
            if day in habit["checkins"]:
                return "already"
            habit["checkins"].append(day)
            storage.save(data)
            return "done"
    return "missing"


if __name__ == "__main__":
    import habits

    habits.add_habit("gym")
    print(check_in("gym"))
    print(check_in("gym"))
    print(check_in("reading"))
