import datetime
import time
exp_date = "2017-07-21"
exp_date =  datetime.date.fromisoformat(exp_date)
todays_Date = datetime.date.fromtimestamp(time.time())
 
# Calling the isoformat() function over the
# today's date and time
DateTime_in_ISOFormat = todays_Date.isoformat()
 
print(DateTime_in_ISOFormat)