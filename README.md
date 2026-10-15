# Habit Builder

A small command-line habit tracker written in Python. Add habits, check in once per day, and see your current streak. Data is saved in a local JSON file, so it survives between runs. No external libraries are needed.

## Requirements

Python 3.8 or newer.

## Usage

```
python main.py add gym        # create a habit
python main.py list           # show all habits
python main.py done gym       # check in for today
python main.py streak gym     # show current streak
```

Example:

```
$ python main.py add gym
Added.
$ python main.py done gym
Checked in for today.
$ python main.py streak gym
gym: 1 day streak
```

A streak counts consecutive days ending today. If you have not checked in yet today, the streak is still alive and counts from yesterday.

## Project structure

| File | Purpose |
| --- | --- |
| `storage.py` | Loads and saves habits in `habits.json` |
| `habits.py` | Adds habits and lists them |
| `checkin.py` | Records a check-in for a day |
| `streak.py` | Calculates the current streak |
| `main.py` | Command-line interface that ties the parts together |

## Data format

```json
{
  "habits": [
    {"name": "gym", "checkins": ["2026-10-14", "2026-10-15"]}
  ]
}
```

## Ideas for later

- Longest streak, not just the current one
- Remove or rename a habit
- Tests with `pytest`
- Serve the same logic through a small FastAPI backend
