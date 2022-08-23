
import requests

def get_output_dict(url):
    r= requests.get(url)
    if r.status_code == 200:
        output_dict = r.json()
    else:
        print("Error")
    return output_dict

def get_hd_titles(output_dict):
    hd_list = output_dict["pvrItems"]
    hd_channels = []
    for item in hd_list:
        format = item["et"]
        if format == "HD":
        #if "hd" in item.keys() and item["hd"]:
         #channel_number = pvrItems["t"]
         channel_number = item["t"]
        hd_channels.append(channel_number)
    return hd_channels

def main():
    url = "http://192.168.0.215:9006/as/pvr?offset=0&limit=1000"
    output_dict = get_output_dict(url)
    hd_titles = get_hd_titles(output_dict)
    print(hd_titles)


if __name__ == "__main__":
    main()