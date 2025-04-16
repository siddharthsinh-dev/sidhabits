from storage import fetch_habits, fetch_all_habits_by_name
from datetime import timedelta

def fetch_all_the_habits():
    ''' Fetch all the Habit Objects from the database '''
    return fetch_habits()

def fetch_habits_by_frequency(frequency):
    ''' Fetch the habits of a particular frequency, Example: Daily Habits Weekly Habits'''
    return [habit for habit in fetch_habits() if habit.frequency.lower() == frequency.lower()]

def fetch_the_longest_streak():
    ''' Fetches the name of the Habit with the longest streak '''
    habits = fetch_habits()
    if not habits:
        return None
    return max(habits, key=lambda x: max(len(x.completion_dates), 0), default=None)

def fetch_longest_streak_for_a_habit(habit_name):
    ''' Fetches the longest streak for a particular habit'''
    def calculate_habit_streak(dates, delta):
        if not dates:
            return 0
        # Use only the dates part of the dates object and sort them
        dates = sorted(set(date.date() for date in dates))
        max_streak = streak = 1
        
        for i in range(1, len(dates)):
            if delta.days == 1: # Daily habit
                if (dates[i] - dates[i-1]).days == 1:
                    streak += 1
                else:
                    streak = 1
            else: # Weekly habit
                if (dates[i] - dates[i-1]).days == 7:
                    streak += 1
                else:
                    streak = 1
            max_streak = max(max_streak, streak)
        return max_streak
    
    habits = fetch_all_habits_by_name(habit_name)
    if not habits:
        return None
    
    delta = timedelta(days=1 if habits[0].frequency.lower() == "daily" else 7)
    all_dates = [date for habit in habits for date in habit.completion_dates]
    return calculate_habit_streak(all_dates, delta)
