# Days counter
A script that counts the total number of days between user adjustable start and end dates.

● The user enters a start date and an end date from the GUI that was implemented using PyQt

● As soon as any day/month/year is changed, the total number of days is updated

● Leap years are also considered

● The program handles invalid user inputs using custom exceptions such as:
	● ensuring that the end date is greater than the start date
	● month values range from 1 to 12
	● only accepting valid dates, for example (31st November or 31st June will not be accepted)
	● only during leap years, the date 29-02-YEAR (29th February) can be entered
	● notifying user if an entry field is left empty	
	● notifying user if any negative value or 0 is entered


# Dependencies:
pip install pyqt5

# Run:
Running days_counter_gui.py will open the GUI