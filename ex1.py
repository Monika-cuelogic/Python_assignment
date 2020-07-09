import datetime
from datetime import date

ageLimit = 100

age = input(" Enter age: ")
name = input(" Enter Name: ")

currDate = datetime.datetime.today()
finalDate = date(currDate.year + (ageLimit - int(age)), 1, 1)

print(f"Hey {name}, You turn 100 yrs old at: {finalDate.strftime('%Y')}")