#find fish with calories greater than 50

import requests

def fish_json_output_dict(url):
    url = "https://www.fishwatch.gov/api/species"
    r = requests.get(url)
    output = r.json()
    return output

def get_fish_cal_names(cal_value=None):
    fish_output = fish_json_output_dict(url = "https://www.fishwatch.gov/api/species")
    species_list = []
    for item in fish_output:
        item_cal_int = int(item["Calories"])
        if item_cal_int> cal_value:
            species_list.append(item["Species Name"])
    return species_list

if __name__ == "__main__":
    cal_fish_names = get_fish_cal_names(cal_value=50)
    print(cal_fish_names)