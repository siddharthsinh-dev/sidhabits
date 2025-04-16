import sqlite3
from datetime import datetime
from habit import Habit

DB_PATH = "habits.db"

def init_db():
    '''' Initialise the database to create the habits table'''
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(''' CREATE TABLE IF NOT EXISTS habits(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                frequency TEXT NOT NULL,
                creation_date TEXT NOT NULL,
                completion_dates TEXT NOT NULL
                )''')
        
def save_habit(habit):
    ''' Save a habit to the database'''
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('INSERT INTO habits (name, frequency, creation_date, completion_dates) VALUES (?, ?, ?, ?)',
                    (habit.name, habit.frequency, habit.creation_date.isoformat(), 
                     str([date.isoformat() for date in habit.completion_dates])))
        return True

def fetch_habits():
    ''' Fetch all habits from the database '''
    habits = []
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute('SELECT * FROM habits')
        for row in cursor:
            habit = Habit(row[1], row[2])
            habit.creation_date = datetime.fromisoformat(row[3])
            # Safely parse the completion dates list
            completion_dates_str = row[4]
            if completion_dates_str and completion_dates_str != '[]':
                dates_list = completion_dates_str.strip('[]').split(', ')
                habit.completion_dates = [datetime.fromisoformat(date.strip("'")) for date in dates_list if date]
            else:
                habit.completion_dates = []
            habits.append(habit)
    return habits
    
def delete_habit(name):
    ''' Deletes a habit from the database. Returns True if the habit was deleted, False otherwise'''
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute("DELETE FROM habits WHERE name = ?", (name,))
        return cur.rowcount > 0

def fetch_habit_by_name(name):
    ''' Fetch a habit by its name from the database '''
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute('SELECT * FROM habits WHERE name = ?', (name,))
        row = cursor.fetchone()
        if row:
            habit = Habit(row[1], row[2])
            habit.creation_date = datetime.fromisoformat(row[3])
            # Safely parse the completion dates list
            completion_dates_str = row[4]
            if completion_dates_str and completion_dates_str != '[]':
                dates_list = completion_dates_str.strip('[]').split(', ')
                habit.completion_dates = [datetime.fromisoformat(date.strip("'")) for date in dates_list if date]
            else:
                habit.completion_dates = []
            return habit
        return None

def fetch_all_habits_by_name(name):
    ''' Fetch all habits with the given name from the database '''
    habits = []
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute('SELECT * FROM habits WHERE name = ?', (name,))
        for row in cursor:
            habit = Habit(row[1], row[2])
            habit.creation_date = datetime.fromisoformat(row[3])
            # Safely parse the completion dates list
            completion_dates_str = row[4]
            if completion_dates_str and completion_dates_str != '[]':
                dates_list = completion_dates_str.strip('[]').split(', ')
                habit.completion_dates = [datetime.fromisoformat(date.strip("'")) for date in dates_list if date]
            else:
                habit.completion_dates = []
            habits.append(habit)
    return habits
    