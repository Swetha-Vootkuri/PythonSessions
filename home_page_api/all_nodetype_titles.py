#if I give you a title iof rail as input and type (nodetype)..find all
import requests

def get_output_dict(url):
    r = requests.get(url)
    if r.status_code == 200:
        output_dict = r.json()
        return output_dict
    else:
        print("Error")

def get_all_nodetype_titles(output_dict):
    all_nodetype_titles=[]
    rail_list = output_dict["slots"][0]["childnodes"]
    for item in rail_list:
         childnodes = item.get("childnodes")
         for item in childnodes:
             if item["nodetype"] == "PROGRAMME":
                all_nodetype_titles.append(item["t"])
    return all_nodetype_titles


def main():
    url = "http://config.skyq-b.interactive.sky.com/config-content-2.x/r27/4101/1/menu?bookmark=HOME_TILES&device=SETTOPBOX&proposition=SKYQ&region=GBR"
    output_dict = get_output_dict(url)
    nodetype_titles = get_all_nodetype_titles(output_dict)
    print(nodetype_titles)


if __name__ == "__main__":
    main()

