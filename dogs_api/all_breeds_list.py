
import requests

def get_json_dog_output_dict(url):
    r = requests.get(url)
    output = r.json()
    return output

#write a function to get all breeds
def get_all_breeds_list():
    dog_output = get_json_dog_output_dict(url = "https://dog.ceo/api/breeds/list/all")
    dog_breeds_list = []
    dog_breed_output = dog_output["message"]
    #print(type(dog_breed_output))
    for breed,sub_breed in dog_breed_output.items():
        print(breed,sub_breed)
        dog_breeds_list.append(breed)
    return dog_breeds_list

#write a function to get particular breed list
def get_subbreeds_list(breed_name = "hound"):
    output = get_json_dog_output_dict(url = "https://dog.ceo/api/breeds/list/all")
    dog_breed_output = output["message"]
    dog_output = dog_breed_output[breed_name]
    return dog_output

#create a list of afghan hound
def get_all_breed_images_list(max=None, breed=None, sub_breed=None):
    url = f"https://dog.ceo/api/breed/{breed}/images"
    output = get_json_dog_output_dict(url=url)
    message_list = output["message"]
    breed_sub_breed_name = f"{breed}-{sub_breed}"
    #print(breed_sub_breed_name)
    sub_breed_list = []
    for image in message_list:
        if breed_sub_breed_name in image:
            sub_breed_list.append(image)
            if len(sub_breed_list) == max:
                break
    return sub_breed_list

if __name__ == "__main__":
   output = get_json_dog_output_dict(url = "https://dog.ceo/api/breeds/list/all")
   dog_breeds_all_list = get_all_breeds_list()
   for breed in dog_breeds_all_list:
       print(breed)
       retriever_breeds = get_subbreeds_list(breed_name= "retriever")
       print(retriever_breeds)
       hound_breeds = get_subbreeds_list(breed_name = "hound")
       print(hound_breeds)
       breed_images = get_all_breed_images_list(max=5,breed="hound",sub_breed="afghan")
       for breed_image in breed_images:
           print(breed_image)
       retriever_images = get_all_breed_images_list(max=3, breed="retriever", sub_breed="chesapeake")
       for retriever_image in retriever_images:
         print(retriever_image)
   bull_dog_dict = {"bulldog":['boston', 'english', 'french']}
   for item in bull_dog_dict["bulldog"]:
     print(f"{item} bulldog")
     sub_breed_full_name = f"{item} bulldog"
     print(sub_breed_full_name)

#Write a func to get all breeds sub_breed full name
