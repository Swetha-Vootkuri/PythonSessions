#write a function to get dog facts

import requests

def get_json_output_dict(api, dog_facts_count=None):
    api = "http://dog-api.kinduff.com/api/facts"
    url = f"{api}?number={dog_facts_count}"
    r = requests.get(url)
    output = r.json()
    return output

def get_all_dog_facts( dog_facts_count = None):
    dog_output = get_json_output_dict(api = "api",dog_facts_count = dog_facts_count)
    print(type(dog_output))
    dog_facts_list = dog_output["facts"]
    return dog_facts_list


if __name__ == "__main__":
    dog_facts_count = 1
    dog_facts = get_all_dog_facts(dog_facts_count = dog_facts_count)
    print(len(dog_facts))

