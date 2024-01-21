# Datetime : A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

import datetime

x = datetime.datetime.now()

print(x)

print(x.year)

print(x.month)

print(x.day)

print(x.strftime("%A")) # The method is called strftime(), and takes one parameter, format, to specify the format of the returned string.

print(datetime.datetime(2020,1,15))   # Create date class and define it's parametres.

print(datetime.date.today())  # Use Module : from datetime import date

print(datetime.date(2003,1,15))

#-----------------------------------------------------------------------------

import time

print(time.time())

print(time.localtime())

print(time.asctime())

print(time.ctime())

print(time.gmtime())

print("Start")
print(time.sleep(2))
print("End")





