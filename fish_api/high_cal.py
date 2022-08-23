#get high cal fish and a func takes dict as input where key is cal and value is 5 and find all fish with carb>5 cal>5

import requests

def fish_json_output_dict(url):
    r = requests.get(url)
    fish_output = r.json()
    return fish_output

def get_all_nutrient_details(cal=None):
    fish_species_output = fish_json_output_dict(url = "https://www.fishwatch.gov/api/species")
    species_details = []
    for item in fish_species_output:
        item_details = item["Carbohydrate"],item["Cholesterol"]
        species_details.append(item_details)
    return species_details