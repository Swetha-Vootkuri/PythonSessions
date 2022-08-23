#write a func if I give a species name and after return carb, cal, chol
import requests

def fish_json_output_dict(url):
    r = requests.get(url)
    fish_output = r.json()
    return fish_output

def get_all_nutrient_details(species_name=None):
    fish_species_output = fish_json_output_dict(url = "https://www.fishwatch.gov/api/species")
    species_details = []
    for item in fish_species_output:
        if species_name:
            item_details = item["Carbohydrate"],item["Cholesterol"]
            species_details.append(item_details)
    return species_details

if __name__ == "__main__":
    fish_nutrients = get_all_nutrient_details(species_name="White Hake")
    print(len(fish_nutrients))


