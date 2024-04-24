### DATES ###
#1. 
from datetime import datetime

now = datetime.now()

print(now)
print(now.timestamp())

#2.
from datetime import datetime
print(now)
formated_date =  now.strftime("%m/%d/%Y, %H:%M:%S")
print(formated_date)

#3.
from datetime import datetime
day_string = "5 December, 2019"
print("day_string =", day_string)
day_object = datetime.strptime(day_string, "%d %B, %Y")
print("day_object =", day_object)

#4.
from datetime import timedelta
from datetime import datetime

time_delta = timedelta()
new_year = datetime(2025, 1, 1)
print(new_year - now)

#5.
from datetime import timedelta
from datetime import datetime

past = datetime (1970, 1, 1)
now =datetime.now()
print(now - past)

#6.
#For checking when exactly an user do something on our app.
