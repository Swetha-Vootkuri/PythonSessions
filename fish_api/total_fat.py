#Find total fat

#Find list of all species which has cholesterol more than 50
import requests

def get_fish_json_dict(url):
    url = "https://www.fishwatch.gov/api/species"
    r = requests.get(url)
    output = r.json()
    return output

def get_all_fatty_fish_species_names(fat_float = None):
    fat_output = get_fish_json_dict(url = "https://www.fishwatch.gov/api/species")
    species_list = []
    for item in fat_output: #"Fat, Total": "1.31 g",
        try:
            fat_list = item["Fat, Total"].split(" ")
        except (KeyError, AttributeError) as e:
            print(e)
            continue
        item_fat_float = float(fat_list[0])
        #print(type(item_fat_float))
        if item_fat_float >= fat_float :
            species_names = item["Species Name"]
            species_list.append(species_names)
    return species_list

if __name__ == "__main__":
    fat_fish = get_all_fatty_fish_species_names(fat_float = 1.31)
    print(fat_fish)
    print(len(fat_fish))



