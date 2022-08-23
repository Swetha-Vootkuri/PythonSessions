#return list of dog pics url

import requests

def get_dog_output_dict(number):
    api = "https://dog.ceo/api/breeds/image/random/"
    url = f"{api}{number}"
    r = requests.get(url)
    output = r.json()
    dog_output = output["message"]
    return dog_output

if __name__ == "__main__":
    print(get_dog_output_dict(number=5))
    print(get_dog_output_dict(number=3))
