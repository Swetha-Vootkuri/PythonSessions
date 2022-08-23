#1.write a function which returns a list of all cities

with open("C:\\Users\\SVI22\\PycharmProjects\\LearnPython\\cities.csv", "r") as fp:
    rows_data = fp.readlines()
    print(rows_data)
    print(type(rows_data))

column_headers_row = rows_data[0].split("\t")
print(column_headers_row)
column_headers = []
for ch in column_headers_row:
    rows = ch.strip().strip('"')
    column_headers.append(rows)
    print(column_headers)
    #print(type(column_headers))
city_index = column_headers.index('City')
print(city_index)

cities_list = []
for row in rows_data:
    cities_list.append(row.split('\t')[city_index])
print(cities_list)