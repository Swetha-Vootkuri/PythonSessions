#Get all childnode titles if input rail as Tailored for you:

import requests

def get_output_dict(url):
    r = requests.get(url)
    if r.status_code == 200:
        output_dict = r.json()
        return output_dict
    else:
        print("Error")

def get_all_childnode_titles(output_dict):
    all_childnode_titles=[]
    rail_list = output_dict["slots"][0]["childnodes"]
    for item in rail_list:
        if item["t"] == "Tailored for you":
            childnodes = item["childnodes"]
            for item in childnodes:
                #print(type(item))
                all_childnode_titles.append(item["t"])
    return all_childnode_titles


def main():
    url = "http://config.skyq-b.interactive.sky.com/config-content-2.x/r27/4101/1/menu?bookmark=HOME_TILES&device=SETTOPBOX&proposition=SKYQ&region=GBR"
    output_dict = get_output_dict(url)
    childnode_title_names = get_all_childnode_titles(output_dict)
    print(childnode_title_names)


if __name__ == "__main__":
    main()

