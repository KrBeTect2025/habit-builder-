"""Part 5: command-line interface that ties everything together.

Usage:
    python main.py add gym
    python main.py list
    python main.py done gym
    python main.py streak gym
"""
import argparse

import checkin
import habits
import storage
import streak


def main():
    parser = argparse.ArgumentParser(description="Simple habit tracker")
    parser.add_argument("command", choices=["add", "list", "done", "streak"])
    parser.add_argument("name", nargs="?", help="habit name")
    args = parser.parse_args()

    if args.command == "list":
        names = habits.list_habits()
        print("\n".join(names) if names else "No habits yet.")
        return

    if not args.name:
        parser.error(f"'{args.command}' needs a habit name")

    if args.command == "add":
        ok = habits.add_habit(args.name)
        print("Added." if ok else "That habit already exists.")

    elif args.command == "done":
        result = checkin.check_in(args.name)
        messages = {
            "done": "Checked in for today.",
            "already": "You already checked in today.",
            "missing": "No such habit. Add it first.",
        }
        print(messages[result])

    elif args.command == "streak":
        name = args.name.strip().lower()
        for habit in storage.load()["habits"]:
            if habit["name"] == name:
                days = streak.current_streak(habit["checkins"])
                print(f"{name}: {days} day streak")
                return
        print("No such habit. Add it first.")


if __name__ == "__main__":
    main()
