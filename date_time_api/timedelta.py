from datetime import datetime,date,timedelta

today_date = datetime.today()
tomorrow_date = today_date + timedelta(days=1)
print(tomorrow_date)
day_after_tomorrow = today_date + timedelta(days = 2)
print(day_after_tomorrow)