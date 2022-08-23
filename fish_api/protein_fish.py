#Find list of all protein fish which has protein more than 1.31g


import requests

def get_fish_json_dict(url):
    url = "https://www.fishwatch.gov/api/species"
    r = requests.get(url)
    output = r.json()
    return output

def get_all_protein_fish_species_names(protein_float = None):
    protein_output = get_fish_json_dict(url = "https://www.fishwatch.gov/api/species")
    species_list = []
    for item in protein_output: #"Fat, Total": "1.31 g",
        try:
            protein_list = item["Protein"].split(" ")
        except (KeyError, AttributeError) as e:
            print(e)
            continue
        item_protein = float(protein_list[0])
        #print(type(item_protein))
        if item_protein >= protein_float :
            species_names = item["Species Name"]
            species_list.append(species_names)
    return species_list

if __name__ == "__main__":
    protein_fish = get_all_protein_fish_species_names(protein_float = 13.89)
    print(protein_fish)
    print(len(protein_fish))






