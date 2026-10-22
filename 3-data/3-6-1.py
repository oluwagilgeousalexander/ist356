
import datetime


my_birthday = "Dec 29th 2005"
my_birthday2 = "2005-12-29"

# today's date 
today = datetime.date.today()

# add 30 days to today
today_plus_30 = today + datetime.timedelta(days=30)

print("Today's date:", today)
print("Today's date plus 30 days:", today_plus_30)

strftime_format = "%A, %B %dth, %Y"
#strftime is for formatting date objects into strings

strptime_format = "%Y-%m-%d"
#strptime is for converting strings into date objects

date_string = datetime.datetime.strftime(today, strftime_format)
print("Today's date is", date_string)

date_object = datetime.datetime.strptime(my_birthday2, strptime_format)
print("My birthday is", date_object)