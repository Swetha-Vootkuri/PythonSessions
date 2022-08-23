#Find app ids of all apps in ap rail

import requests

def get_output_dict(url):
    r = requests.get(url)
    if r.status_code == 200:
        output_dict = r.json()
        return output_dict
    else:
        print("Error")

def get_all_app_ids(output_dict):
    all_app_ids = []
    rail_list = output_dict["slots"][0]["childnodes"]
    for item in rail_list:
        if item["t"] == "Apps & inputs":
            childnodes = item["childnodes"]
            for item in childnodes:
               all_app_ids.append(item["appid"])
    return all_app_ids

def main():
    url = "http://config.skyq-b.interactive.sky.com/config-content-2.x/r27/4101/1/menu?bookmark=HOME_TILES&device=SETTOPBOX&proposition=SKYQ&region=GBR"
    output_dict = get_output_dict(url)
    app_ids = get_all_app_ids(output_dict)
    print(app_ids)


if __name__ == "__main__":
    main()