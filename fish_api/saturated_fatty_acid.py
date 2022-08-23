#input "Saturated Fatty Acids, Total", output should be Total,Saturated Fatty Acids

import requests

def fish_json_output_dict(url):
    r = requests.get(url)
    fish_output = r.json()
    return fish_output

def get_reverse_output():
    fish_output = fish_json_output_dict(url ="https://www.fishwatch.gov/api/species" )
    for item in fish_output:
        item_list = item["Saturated Fatty Acids, Total"].split(" ")
        list_reverse = list(reversed(item_list))
        return list_reverse

def get_reverse_of_string():
    fish_saturated = "Saturated Fatty Acids, Total"
    split_fish_saturated = fish_saturated.split(",")
    print(split_fish_saturated)
    reverse_split_fish_saturated = split_fish_saturated.reverse()
    join_fish_saturated = ' '.join(split_fish_saturated)
    print(join_fish_saturated)


if __name__ == "__main__":
  get_reverse_output()
  get_reverse_of_string()


