#All the titles of the page

import requests

def get_output_dict(url):
    r = requests.get(url)
    if r.status_code == 200:
        output_dict = r.json()
        return output_dict
    else:
        print("Error")

def get_all_page_titles(output_dict):
    items = output_dict.get("t")
    return items



def main():
    url = "http://config.skyq-b.interactive.sky.com/config-content-2.x/r27/4101/1/menu?bookmark=HOME_TILES&device=SETTOPBOX&proposition=SKYQ&region=GBR"
    output_dict = get_output_dict(url)
    page_titles = get_all_page_titles(output_dict)
    print(page_titles)

if __name__ == "__main__":
    main()


