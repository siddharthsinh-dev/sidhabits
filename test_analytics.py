import unittest
from datetime import datetime
from habit import Habit
from storage import save_habit, init_db, fetch_habits
from analytics import fetch_all_the_habits, fetch_habits_by_frequency, fetch_the_longest_streak, fetch_longest_streak_for_a_habit
import sqlite3

class TestAnalytics(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        ''' Initialize the database and save a few habits for testing'''
        init_db()

    def setUp(self):
        ''' Add test habits to the database'''
        self.fetch_predefined_habits()

    def create_test_habits(self, name, frequency, completion_dates):
        habit = Habit(name, frequency)
        habit.completion_dates = [datetime.strptime(date, "%Y-%m-%d") for date in completion_dates]
        save_habit(habit)

    def fetch_predefined_habits(self):
        habits_data = [
        ("yoga", "daily", ["2025-03-01", "2025-03-02", "2025-03-03", "2025-03-04", "2025-03-05", "2025-03-06", "2025-03-07", "2025-03-08", "2025-03-09", "2025-03-10", "2025-03-11", "2025-03-12", "2025-03-13", "2025-03-14", "2025-03-15", "2025-03-16", "2025-03-17", "2025-03-18", "2025-03-19", "2025-03-20", "2025-03-21", "2025-03-22", "2025-03-23", "2025-03-24", "2025-03-25", "2025-03-26", "2025-03-27", "2025-03-28", "2025-03-29", "2025-03-30", "2025-03-31"]),

        ("exercise", "daily", ["2025-03-03", "2025-03-04", "2025-03-05", "2025-03-06", "2025-03-07", "2025-03-10", "2025-03-11", "2025-03-12", "2025-03-13", "2025-03-14", "2025-03-17", "2025-03-18", "2025-03-19", "2025-03-20", "2025-03-21", "2025-03-24", "2025-03-25", "2025-03-26", "2025-03-27", "2025-03-28", "2025-03-31"]),

        ("journaling", "daily", ["2025-03-03", "2025-03-04", "2025-03-05", "2025-03-06", "2025-03-09", "2025-03-10", "2025-03-11", "2025-03-17", "2025-03-18", "2025-03-19", "2025-03-20", "2025-03-21", "2025-03-25", "2025-03-26", "2025-03-27", "2025-03-30", "2025-03-31"]),

        ("car washing", "weekly", ["2025-03-01", "2025-03-08", "2025-03-15", "2025-03-22", "2025-03-29"]),

        ("play golf", "weekly", ["2025-03-02", "2025-03-09", "2025-03-16", "2025-03-23", "2025-03-30"])
        ]

        for name, frequency, dates in habits_data:
            self.create_test_habits(name, frequency, dates)

    def assertHabitNames(self, habits, expected_names):
        names = {habit.name for habit in habits}
        for name in expected_names:
            self.assertIn(name, names)

    def test_fetch_all_habits(self):
        habits = fetch_all_the_habits()
        self.assertHabitNames(habits, ["yoga", "exercise", "journaling", "car washing", "play golf"])

    def test_fetch_habits_by_frequency_daily(self):
        daily_habits = fetch_habits_by_frequency("daily")
        self.assertHabitNames(daily_habits, ["yoga", "exercise", "journaling"])

    def test_fetch_habits_by_frequency_weekly(self):
        weekly_habits = fetch_habits_by_frequency("weekly")
        self.assertHabitNames(weekly_habits, ["car washing", "play golf"])

    def test_fetch_the_longest_streak(self):
        habit = fetch_the_longest_streak()
        self.assertEqual(habit.name, "yoga")

    def test_fetch_longest_streak_for_a_habit(self):
        streak = fetch_longest_streak_for_a_habit("yoga")
        self.assertEqual(streak, 31)

    def test_single_habit_streak(self):
        """Test streak calculation for a single habit with consecutive dates"""
        self.create_test_habits("reading", "daily", ["2025-03-01", "2025-03-02", "2025-03-03", "2025-03-04", "2025-03-05"])
        streak = fetch_longest_streak_for_a_habit("reading")
        self.assertEqual(streak, 5)

if __name__ == "__main__":
    unittest.main()