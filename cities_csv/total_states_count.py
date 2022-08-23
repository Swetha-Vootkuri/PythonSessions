#1.write a function which returns total num of states

with open("C:\\Users\\SVI22\\PycharmProjects\\LearnPython\\cities.csv", "r") as fp:
        rows_data = fp.readlines()
        print(type(rows_data))


column_headers_row = rows_data[0].split("\t")
print(type(column_headers_row))
column_headers = []
for ch in column_headers_row:
    column_headers.append(ch.strip().strip('"'))
    print(type(column_headers))
state_index = column_headers.index('State')
print(type(state_index))

states_list = []
for row in rows_data:
    rows = row.strip('"').strip("\n").lstrip()
    states_list.append(rows.split('\t')[state_index])
print(states_list)

states_count = 0
for state in states_list:
    states_count += 1
print(states_count)

#or

states_count = len(states_list)
print(states_count)

