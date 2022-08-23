from datetime import datetime

time_today = datetime(2022,8,18,22,15,12,23456)
print(time_today)

#or
from datetime import datetime,time

time_now = datetime.today().time()
print(time_now)
