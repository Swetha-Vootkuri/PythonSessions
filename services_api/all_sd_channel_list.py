#3.Write a function to return a list of all SD channels

import requests

def get_output_dict(url):
    r = requests.get(url)
    if r.status_code == 200:
        output_dict = r.json()
        return output_dict
    else:
        print("Error")
def get_all_sd_channel_names(output_dict):
    all_sd_channel_names=[]
    sd_list = output_dict["services"]
    for service in sd_list:
        if service["sf"] == "sd":
            all_sd_channel_names.append(service["t"])
    return all_sd_channel_names


def main():
    url = "http://192.168.0.215:9006/as/services"
    output_dict = get_output_dict(url)
    sd_channel_names = get_all_sd_channel_names(output_dict)
    print(sd_channel_names)


if __name__ == "__main__":
    main()

