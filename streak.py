"""Part 4: streak counting."""
from datetime import date, timedelta


def current_streak(checkins, today=None):
    """Count consecutive days ending today (or yesterday).

    If you have not checked in yet today, the streak is still alive:
    you have until midnight. So we start counting from yesterday then.
    """
    today = today or date.today()
    done = set(checkins)  # a set makes "is this day in the list?" fast

    day = today
    if day.isoformat() not in done:
        day = day - timedelta(days=1)

    streak = 0
    while day.isoformat() in done:
        streak += 1
        day = day - timedelta(days=1)
    return streak


if __name__ == "__main__":
    today = date(2026, 10, 15)
    print(current_streak(["2026-10-13", "2026-10-14", "2026-10-15"], today))  # 3
    print(current_streak(["2026-10-13", "2026-10-14"], today))                # 2
    print(current_streak(["2026-10-10", "2026-10-11"], today))                # 0
    print(current_streak([], today))                                          # 0
