from storage import init_db, save_habit, fetch_habits, delete_habit, DB_PATH
from habit import Habit
from analytics import fetch_all_the_habits, fetch_habits_by_frequency, fetch_the_longest_streak, fetch_longest_streak_for_a_habit 
from predefined_habits import predefined_habits
import sqlite3

print("Welcome to SIDHABITS : Your Personal Go-To Habit Tracker")

def main_menu():
    ''' This function will display the main menu and handle the user's input '''
    while True:
        print("\nMain Menu:")
        print("1. Add a new habit")
        print("2. View all habits")
        print("3. Complete a habit")
        print("4. Analyze Habits")
        print("5. Delete a habit")
        print("6. Exit Application")

        choice = input("Enter your choice: ").strip().lower()

        if choice == "1":
            add_new_habit()
        elif choice == "2":
            view_all_habits()
        elif choice == "3":
            complete_a_habit()
        elif choice == "4":
            analyze_habits()
        elif choice == "5":
            delete_a_habit()
        elif choice == "6":
            print("Exiting the application.")
            print("Thankyou for using SIDHABITS. Goodbye! Work Hard, Stay Strong, and Keep Hustling!")
            break
        else:
            print("Invalid choice. Please select a valid option from the menu.")

def add_new_habit():
    '''' This function will add a new habit along with its frequency to the database'''
    name = input("Enter the name of the habit:").strip().lower()
    
    while True:
        frequency = input("Enter the frequency of the habit (daily, weekly):").strip().lower()
        if frequency in ['daily', 'weekly']:
            break
        print("Invalid frequency. Please enter either 'daily' or 'weekly'.")

    if any(x.name == name for x in fetch_habits()):
        print(f"Habit '{name}' already exists. Please choose a different name.")
        return
    
    habit = Habit(name, frequency)
    save_habit(habit)
    print(f"Habit '{name}' with frequency '{frequency}' has been added successfully.")

def view_all_habits():
    ''' This function will display all the habits in the database '''
    habits = fetch_habits()
    printed = set()
    for habit in habits:
        if habit.name not in printed:
            print(habit)
            printed.add(habit.name)

def complete_a_habit():
    ''' This function will allow the user to mark a habit as completed'''
    name = input("Enter the name of the habit to be marked as completed:").strip().lower()
    habits = fetch_habits()
    for habit in habits:
        if habit.name == name:
            if habit.complete_a_habit():
                print(f"Habit '{name}' has been marked as completed.")
                # Update the habit in the database
                with sqlite3.connect(DB_PATH) as conn:
                    conn.execute('UPDATE habits SET completion_dates = ? WHERE name = ?',
                               (str([date.isoformat() for date in habit.completion_dates]), name))
            return
    print(f"Habit '{name}' not found. Please check the name and try again.")

def delete_a_habit():
    ''' This function will allow the user to delete a habit from the database '''
    name = input("Enter the name of the habit to be deleted:").strip().lower()
    if delete_habit(name):
        print(f"Habit '{name}' has been deleted successfully.")
    else:
        print(f"Habit '{name}' not found. Please check the name and try again.")

def analyze_habits():
    ''' This function will allow the user to analyze the habits by frequency, longest streak, and longest streak for a habit '''
    print("\nAnalyze Habits:")
    print("1. Fetch all habits")
    print("2. Fetch habits by frequency")
    print("3. Fetch the longest streak")
    print("4. Fetch the longest streak for a habit")

    choice = input("Enter your choice:").strip().lower()

    if choice == "1":
        habits = fetch_all_the_habits()
        for habit in habits:
            print(habit)
    elif choice == "2":
        frequency = input("Enter the frequency of the habit (daily, weekly):").strip().lower()
        habits = fetch_habits_by_frequency(frequency)
        for habit in habits:
            print(habit)
    elif choice == "3":
        habit = fetch_the_longest_streak()
        if habit:
            print(f"Longest Streak: {habit.name} with {len(habit.completion_dates)} completions")
        else:
            print("No habit found")
    elif choice == "4":
        name = input("Enter the name of the habit:").strip().lower()
        streak = fetch_longest_streak_for_a_habit(name)
        if streak is not None:
            print(f"Longest Streak for '{name}': {streak} days")
        else:
            print(f"No streak data found for habit '{name}'")
    else:
        print("Invalid choice. Please select a valid option from the menu.")

'''This is the main function that will initialise the database, add predefined habits and display the main menu'''
if __name__ == '__main__':
    init_db()
    predefined_habits()
    main_menu()
