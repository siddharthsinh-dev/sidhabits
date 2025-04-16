from datetime import datetime

class Habit:
    def __init__(self,name,frequency):
        ''' Initialize the Habit Object 
        
        Parameters:
            name (str): The name of the habit
            frequency (str): The frequency of the habit (Daily or Weekly)
        '''
        self.name = name
        self.frequency = frequency
        self.creation_date = datetime.now().replace(microsecond=0)
        self.completion_dates = []
    
    def complete_a_habit(self):
        ''' This method is used to complete a habit
        Returns:
            bool: True if the habit was completed, False if it was already completed
        '''
        today = datetime.now().replace(microsecond=0).date()
        if any(date.date() == today for date in self.completion_dates):
            print(f"Habit {self.name} is already marked as completed today")
            return False
        self.completion_dates.append(datetime.now().replace(microsecond=0))
        return True
    
    def __repr__(self):
        ''' This method will represent the habit in a string format '''
        return (f"Habit(name = {self.name}, frequency = {self.frequency}, creation_date = {self.creation_date}, completion_dates = {self.completion_dates})")
    
    def __str__(self):
        ''' This method will format the habit in a string format that is visually appealing and can be printed to the user'''
        if self.completion_dates:
            completion_dates_str = ",".join(str(date.strftime("%Y-%m-%d %H:%M:%S")) for date in self.completion_dates)
        else:
            completion_dates_str = "No completion dates yet"

        return (f"Habit : {self.name} \n"
                f"Frequency : {self.frequency} \n"
                f"Creation Date : {self.creation_date} \n"
                f"Completion Dates : {completion_dates_str}")
    