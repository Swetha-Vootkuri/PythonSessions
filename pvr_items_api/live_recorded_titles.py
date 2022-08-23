# To Return all linear(LIve) recorded titles

import requests

def get_output_dict(url):
    r = requests.get(url)
    if r.status_code == 200:
        output_dict = r.json()
        return output_dict
    else:
        print("Error")

def get_live_titles(output_dict):
    live_titles= []
    items = output_dict["pvrItems"]
    for item in items:
        if item["src"] == "LIVE":
            live_titles.append(item["t"])
    return live_titles


def main():
    url = "http://192.168.0.181:9006/as/pvr?offset=0&limit=1000"
    output_dict = get_output_dict(url)
    recorded_live_titles = get_live_titles(output_dict)
    print(recorded_live_titles)

if __name__ == "__main__":
    main()
