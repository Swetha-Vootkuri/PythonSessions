#6.Write a func to return genres of a particular type

import requests

def get_output_dict(url):
    r = requests.get(url)
    if r.status_code == 200:
        output_dict = r.json()
        return output_dict
    else:
        print("Error")

def get_all_genres_particulars(output_dict):
    genres_titles=[]
    genres_list = output_dict["genres"]
    for genre in genres_list:
        if genre["t"] == "Shopping":
            genres_titles.append(genre["t"])
    return genres_titles


def main():
    url = "http://192.168.0.215:9006/as/services/genres"
    output_dict = get_output_dict(url)
    genres_title = get_all_genres_particulars(output_dict)
    print(genres_title)


if __name__ == "__main__":
    main()

