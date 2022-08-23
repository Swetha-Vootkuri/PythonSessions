#

import requests

def get_output_dict(url):
    r = requests.get(url)
    if r.status_code == 200:
        output_dict = r.json()
        return output_dict
    else:
        print("Error")

def get_all_logos(output_dict):
    all_logos = []
    rail_list = output_dict["slots"][0]["childnodes"]
    for item in rail_list:
        item_keys = item.keys()
        all_logos.append(item_keys)
         #print(item.keys())

    return all_logos

def main():
    url = "http://config.skyq-b.interactive.sky.com/config-content-2.x/r27/4101/1/menu?bookmark=HOME_TILES&device=SETTOPBOX&proposition=SKYQ&region=GBR"
    output_dict = get_output_dict(url)
    logos = get_all_logos(output_dict)
    print(logos)


if __name__ == "__main__":
    main()