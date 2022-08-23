from datetime import *

date_today = date.today()
group_dates = []
group_dates.append(date_today)
date = date(2022,8,8)
group_dates.append(date)
group_dates.append(date + timedelta(days=5))
group_dates.sort()
for date in group_dates:
    print(date)
