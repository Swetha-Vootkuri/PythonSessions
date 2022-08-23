from datetime import datetime

print(datetime.today())


#or

now_1 = datetime.now()
print(now_1)
example_1 = now_1.strftime("%a %m %y")
print(example_1)

time_data = ["25/05/99 02:35:8.023", "26/05/99 12:45:0.003",
             "27/05/99 07:35:5.523", "28/05/99 05:15:55.523"]

format_data = "%d/%m/%y %H:%M:%S.%f"

for i in time_data:
    print(datetime.strptime(i,format_data))
