#write a function which returns list of cities in a state provided the argument is a State



def file_open(file_name):
    with open(file_name, "r") as fp:
        rows_data = fp.readlines()
    return rows_data

'''state_name =  split the line and take the last element
city_name  = split the line and take the second last element
compare state_name with the input state
'''

def list_of_cities_in_state(file_name,state):
    city_list_names= []
    rows_data = file_open(file_name)
    rows_data = rows_data[1:]
    for row in rows_data:
        state_name = row.split("\t")[-1].strip()
        #print(state_name)
        #print(state)
        if state_name == state:
            city_name = row.split("\t")[-2].strip().strip('"')
            #print(city_name)
            city_list_names.append(city_name)

    return city_list_names


def main():
    file_name = "C:\\Users\\SVI22\\PycharmProjects\\LearnPython\\cities.csv"
    state = "OH"
    city_list = list_of_cities_in_state(file_name,state)
    print(city_list)


if __name__ == "__main__":
    main()

