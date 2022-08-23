#Find list of all sub_breed breed name
import requests

def get_json_dog_output_dict(url):
    r = requests.get(url)
    output = r.json()
    return output

def get_breed_sub_breed_full_name():
    dog_output = get_json_dog_output_dict(url = "https://dog.ceo/api/breeds/list/all")
    dog_breed_output = dog_output["message"]

    dog_full_name = dog_breed_output.items()
    for breed, sub_breeds in dog_full_name:
        # print(f"breed:{breed}; type:{sub_breed}")
        # print(f"{sub_breed} {breed}")
        if sub_breeds:
            for sub_breed in sub_breeds:
                print(f"{sub_breed}-{breed}")
        else:
            print(f"{breed}")


if __name__ == "__main__":
   output = get_json_dog_output_dict(url = "https://dog.ceo/api/breeds/list/all")
   dog_keys_fullname = get_breed_sub_breed_full_name()
   #print(dog_keys_fullname)

