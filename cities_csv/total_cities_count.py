#1.write a function which returns total num of cities

with open("C:\\Users\\SVI22\\PycharmProjects\\LearnPython\\cities.csv", "r") as fp:
        rows_data = fp.readlines()
        print(rows_data)

column_headers_row = rows_data[0].split("\t")
print(type(column_headers_row))
column_headers = []
for ch in column_headers_row:
    column_headers.append(ch.strip().strip('"'))
    print(type(column_headers))
city_index = column_headers.index('City')
print(city_index)

cities_list = []
for row in rows_data:
    cities_list.append(row.split('\t')[city_index])
print(cities_list)

city_count = 0
for city in cities_list:
    city_count += 1
print(city_count)

#or
print(len(cities_list))

