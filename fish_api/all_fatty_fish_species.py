#Find list of all species which has cholesterol more than 50
import requests

def get_fish_json_dict(url):
    r = requests.get(url)
    output = r.json()
    return output

def get_all_fatty_fish_species_names(cholesterol_int = None):
    output = get_fish_json_dict(url = "https://www.fishwatch.gov/api/species")
    species_list = []
    for item in output:
        try:
            cholesterol_list = item["Cholesterol"].split(" ")
        except (KeyError, AttributeError) as e:
            print(e)
            continue
        item_cholesterol_int = int(cholesterol_list[0])
        #print(type(item_cholesterol_int))
        if item_cholesterol_int >= cholesterol_int :
             species_names = item["Species Name"]
             species_list.append(species_names)
    return species_list

if __name__ == "__main__":
    fatty_fish = get_all_fatty_fish_species_names(cholesterol_int = 50)
    print(fatty_fish)



