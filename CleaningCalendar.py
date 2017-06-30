import datetime
import calendar


daynumber = datetime.datetime.now().day
weeknumber = (daynumber - 1) // 7 + 1
weekday = datetime.date.today().strftime("%A")
month = datetime.date.today().strftime("%B")
print daynumber
print weeknumber
print weekday
print month
