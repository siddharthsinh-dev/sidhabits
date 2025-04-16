import pytest
from habit import Habit
from storage import save_habit, fetch_habits, init_db, delete_habit, fetch_habit_by_name

@pytest.fixture(autouse=True)
def setup_and_teardown():
    ''' Initialize the database and ensure it's empty'''
    init_db()
    delete_habit("Test Habit")
    yield
    delete_habit("Test Habit")

def test_create_habit():
    ''' Test that a habit is created successfully'''
    habit = Habit("Test Habit", "daily")
    assert habit.name == "Test Habit"
    assert habit.frequency == "daily"
    assert habit.completion_dates == []

def test_complete_habit():
    ''' Test that a habit can be completed and its completion date is recorded'''
    habit = Habit("Test Habit", "daily")
    habit.complete_a_habit()
    assert len(habit.completion_dates) == 1

def test_save_and_fetch_habit():
    ''' Test saving and fetching a habit to and from the database'''
    habit = Habit("Test Habit", "daily")
    save_habit(habit)
    habits = fetch_habits()
    assert any(habit.name == "Test Habit" for habit in habits)