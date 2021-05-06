import datetime

# How to use Function import datetime of today's date and time from Python-Programming Datetime

# defining the datetime_object of the current date
datetime_object = datetime.datetime.now()

# defining the date_object of the current time
date_object = datetime.date.today()

# showing the output of the date and Time
print(datetime_object)
print (date_object)

#Display date object of today's date_objecttoday = date.today() from import datetime

from datetime import date
today = date.today()
print("Currentyear:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)