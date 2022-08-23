import requests

def get_output_dict(url):
    r = requests.get(url)
    if r.status_code == 200:
        output_dict = r.json()
        return output_dict
    else:
        print("Error")

def get_all_pvr_titles_names(output_dict):
    pvr_titles = []
    items = output_dict["pvrItems"]
    for item in items:
       pvr_titles.append(item["t"])
    return pvr_titles

def main():
    url = "http://192.168.0.215:9006/as/pvr?offset=0&limit=1000"
    output_dict = get_output_dict(url)
    pvr_titles_genres = get_all_pvr_titles_names(output_dict)
    print(pvr_titles_genres)

if __name__ == "__main__":
    main()