from habit import Habit
from storage import save_habit, fetch_habits
from datetime import datetime

def predefined_habits():
    ''' This will add predefined habits to the database'''
    def parse_date(date_list):
        return [datetime.strptime(date_str, "%Y-%m-%d") for date_str in date_list]

    habits_data = [
        ("yoga", "daily", ["2025-03-01", "2025-03-02", "2025-03-03", "2025-03-04", "2025-03-05", "2025-03-06", "2025-03-07", "2025-03-08", "2025-03-09", "2025-03-10", "2025-03-11", "2025-03-12", "2025-03-13", "2025-03-14", "2025-03-15", "2025-03-16", "2025-03-17", "2025-03-18", "2025-03-19", "2025-03-20", "2025-03-21", "2025-03-22", "2025-03-23", "2025-03-24", "2025-03-25", "2025-03-26", "2025-03-27", "2025-03-28", "2025-03-29", "2025-03-30", "2025-03-31"]),

        ("exercise", "daily", ["2025-03-03", "2025-03-04", "2025-03-05", "2025-03-06", "2025-03-07", "2025-03-10", "2025-03-11", "2025-03-12", "2025-03-13", "2025-03-14", "2025-03-17", "2025-03-18", "2025-03-19", "2025-03-20", "2025-03-21", "2025-03-24", "2025-03-25", "2025-03-26", "2025-03-27", "2025-03-28", "2025-03-31"]),

        ("journaling", "daily", ["2025-03-03", "2025-03-04", "2025-03-05", "2025-03-06", "2025-03-09", "2025-03-10", "2025-03-11", "2025-03-17", "2025-03-18", "2025-03-19", "2025-03-20", "2025-03-21", "2025-03-25", "2025-03-26", "2025-03-27", "2025-03-30", "2025-03-31"]),

        ("car washing", "weekly", ["2025-03-01", "2025-03-08", "2025-03-15", "2025-03-22", "2025-03-29"]),

        ("play golf", "weekly", ["2025-03-02", "2025-03-09", "2025-03-16", "2025-03-23", "2025-03-30"])
    ]

    existing_habits = fetch_habits()
    existing_names = {h.name.lower() for h in existing_habits}

    for name, frequency, dates in habits_data:
        if name.lower() not in existing_names:
            habit = Habit(name, frequency)
            parsed_dates = parse_date(dates)
            habit.completion_dates = parsed_dates
            habit.creation_date = parsed_dates[0]
            save_habit(habit)