# SIDHABITS

A powerful and intuitive habit tracking application built with Python that helps users create, track, and analyze their daily and weekly habits.

## Overview

SIDHABITS is a Python-based habit tracking application that enables users to effectively manage their daily and weekly goals. The application provides a simple command-line interface for creating, tracking, updating, and analyzing habits, making it easy to build and maintain positive routines. Built with object-oriented and functional programming principles, SIDHABITS offers a easy to use and reliable solution for habit tracking.

## Features

- **Create Habits**: Add new habits with customizable periodicities (daily/weekly)
- **View & Complete Habits**: Mark habits as complete and track completion dates
- **View Habits**: List all available habits with their details
- **Analyze Performance**: Get insights about your habits including:
  - View all habits
  - Filter habits by frequency
  - Track longest streaks
  - Analyze individual habit performance
- **Manage Habits**: Delete habits you no longer want to track
- **Predefined Habits**: Predefined habits created for functionality testing

## Requirements

- Python 3.8 or higher
- SQLite3 (included in Python standard library)
- pytest (for running tests)

## Installation

### Option 1: Clone the Repository

If you have Git installed:

```bash
# Clone the repository
git clone "https://github.com/siddharthsinh-dev/sidhabits.git"

# Navigate to the project directory
cd "sidhabits"

# Install dependencies
pip install pytest
```

### Option 2: Manual Download

1. Visit the GitHub repository: "https://github.com/siddharthsinh-dev/sidhabits.git"
2. Click the "Code" button and select "Download ZIP File"
3. Extract the ZIP file to your desired location
4. Open a terminal and navigate to the extracted folder:
   ```bash
   cd sidhabits
   ```
5. Install the required dependencies:
   ```bash
   pip install pytest
   ```

## Usage

To start the application:

```bash
python main.py
```

The application will present you with a main menu offering the following options:

1. **Add a new habit**: Create a new habit with a name and frequency (daily/weekly)
2. **View all habits**: See a list of all your tracked habits
3. **Complete a habit**: Mark a habit as completed for the current day
4. **Analyze Habits**: Access various analytics features:
   - View all habits
   - Filter habits by frequency
   - Check longest streaks
   - Analyze individual habit performance
5. **Delete a habit**: Remove a habit from your tracker
6. **Exit Application**: Close the application

## Project Structure

The project follows a modular design with the following components:

- `main.py`: The main application file containing the command-line interface and menu system
- `habit.py`: Defines the `Habit` class with properties and methods for habit management
- `storage.py`: Handles all database operations using SQLite
- `analytics.py`: Provides functions for analyzing habit data and generating insights
- `predefined_habits.py`: Contains pre-defined habits that can be added to the tracker
- `test_habit_tracker.py`: Unit tests for the main habit tracking functionality
- `test_analytics.py`: Unit tests for the analytics module
- `habits.db`: SQLite database file for storing habit data

## Testing

To run the test suite:

```bash
pytest test_habit_tracker.py test_analytics.py
```

The test suite includes:
- Unit tests for habit creation and management
- Tests for analytics functionality
- Database operation tests

## About Project

This project was created by Siddharthsinh Rathod as the Portfolio project for the course of Object Oriented and Functional Programming with Python at IU (International University of Applied Sciences) in April 2025.