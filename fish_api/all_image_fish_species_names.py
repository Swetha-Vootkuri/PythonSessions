#Find list of all species which has image gallery
import requests

def get_fish_json_dict(url):
    r = requests.get(url)
    output = r.json()
    return output

def get_all_image_fish_species_names():
    output = get_fish_json_dict(url = "https://www.fishwatch.gov/api/species")
    species_list = []
    for item in output:
        if item["Image Gallery"]:
            species_names = item["Species Name"]
            species_list.append(species_names)
    return species_list

if __name__ == "__main__":
    all_species_names = get_all_image_fish_species_names()
    print(all_species_names)


