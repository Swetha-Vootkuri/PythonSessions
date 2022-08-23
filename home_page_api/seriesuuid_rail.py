import requests

def get_output_dict(url):
    r = requests.get(url)
    if r.status_code == 200:
        output_dict = r.json()
        return output_dict
    else:
        print("Error")

def get_all_seriesuuid(output_dict):
    all_seriesuuid=[]
    rail_list = output_dict["slots"][0]["childnodes"]
    for item in rail_list:
        childnodes = item["childnodes"]
        for item in childnodes:
            if item["nodetype"] == "SERIES":
              all_seriesuuid.append(item["seriesuuid"])
    return all_seriesuuid


def main():
    url = "http://config.skyq-b.interactive.sky.com/config-content-2.x/r27/4101/1/menu?bookmark=HOME_TILES&device=SETTOPBOX&proposition=SKYQ&region=GBR"
    output_dict = get_output_dict(url)
    seriesuuid_text = get_all_seriesuuid(output_dict)
    print(seriesuuid_text)


if __name__ == "__main__":
    main()


