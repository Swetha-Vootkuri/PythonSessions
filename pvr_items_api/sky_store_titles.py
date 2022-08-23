#All Sky Store titles

import requests

def get_output_dict(url):
    r= requests.get(url)
    if r.status_code == 200:
        output_dict = r.json()
    else:
        print("Error")
    return output_dict

def get_sky_store_titles(output_dict):
    sky_store_titles=[]
    items= output_dict["pvrItems"]
    for item in items:
        #if item["cn"] == "Sky Store":
        if "Sky Store" in item.values() and item["Sky Store"]:
            sky_store_titles.append(item["t"])
    return sky_store_titles

def main():
    url = "http://192.168.0.215:9006/as/pvr?offset=0&limit=1000"
    output_dict = get_output_dict(url)
    sky_store_titles_names = get_sky_store_titles(output_dict)
    print(sky_store_titles_names)


if __name__ == "__main__":
    main()