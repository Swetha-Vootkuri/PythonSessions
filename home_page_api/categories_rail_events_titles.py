#categories rail,Give me tvshows, movies


import requests

def get_output_dict(url):
    r = requests.get(url)
    if r.status_code == 200:
        output_dict = r.json()
        return output_dict
    else:
        print("Error")

def get_all_categories_rail_event_titles(output_dict):
    categories_rail_event_titles = []
    rail_list = output_dict["slots"][0]["childnodes"]
    for item in rail_list:
        if item["t"] == "Categories":
            childnodes = item["childnodes"]
            for item in childnodes:
                categories_rail_event_titles.append(item["t"])
    return categories_rail_event_titles

def main():
    url = "http://config.skyq-b.interactive.sky.com/config-content-2.x/r27/4101/1/menu?bookmark=HOME_TILES&device=SETTOPBOX&proposition=SKYQ&region=GBR"
    output_dict = get_output_dict(url)
    categories_event_titles = get_all_categories_rail_event_titles(output_dict)
    print(categories_event_titles)


if __name__ == "__main__":
    main()