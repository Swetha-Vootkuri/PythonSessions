
import requests

def get_output_dict(url):
    r= requests.get(url)
    if r.status_code == 200:
        output_dict = r.json()
        return output_dict
    else:
        print("Error")


def get_all_download_links(output_dict):
    download_link = output_dict["pvrItems"]
    download_all_links = []
    for item in download_link:
        if int(item["eg"]) == 6:
            download_all_links.append(item["downloadlink"])
    return download_all_links


def main():
    url = "http://192.168.0.181:9006/as/pvr?offset=0&limit=1000"
    output_dict = get_output_dict(url)
    download_all_item_links = get_all_download_links(output_dict)
    print(download_all_item_links)


if __name__ == "__main__":
    main()