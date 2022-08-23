#1.write a function which returns a list of all states

with open("C:\\Users\\SVI22\\PycharmProjects\\LearnPython\\cities.csv", "r") as fp:
        rows_data = fp.readlines()

column_headers_row = rows_data[0].split("\t")
print(type(column_headers_row))
column_headers = []
for ch in column_headers_row:
    rows = ch.strip().strip('"')
    column_headers.append(rows)
    print(type(column_headers))
state_index = column_headers.index('State')
print(state_index)

states_list = []
for row in rows_data:
    rows = row.strip('"').strip("\n").lstrip()
    states_list.append(rows.split('\t')[state_index])
print(states_list)



