import datetime

today_date = datetime.date.today() #gives today date
print(today_date)

#or

from datetime import date    #gives today date
today_date = date.today()
print(today_date)

#or
import datetime   #gives today date with time
today_date_time = datetime.datetime.today()
today_date_time_1 = datetime.datetime.now()
print(today_date_time)
print(today_date_time_1)

#or
from datetime import datetime , date
today = date.today()
print(today)

#or
import datetime

today_date = date.today()
print(today_date)
today_date = datetime.date(2022, 8, 18)
print(today_date)

#get date from timestamp

from datetime import datetime, date

today_date = date.fromtimestamp(202020200)
print(today_date)


