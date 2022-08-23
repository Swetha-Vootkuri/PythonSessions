#2.Write a function to return all the channels whose sids<3000

import requests

def get_output_dict(url):
    r = requests.get(url)
    if r.status_code == 200:
        output_dict = r.json()
        return output_dict
    else:
        print("Error")

def get_all_channel_names(output_dict):
    channel_names=[]
    services_list = output_dict["services"]
    for service in services_list:
        if int(service["sid"]) < 3000:
            channel_names.append(service["t"])
    return channel_names


def main():
    url = "http://192.168.0.215:9006/as/services"
    output_dict = get_output_dict(url)
    sid_channel_names = get_all_channel_names(output_dict)
    print(sid_channel_names)



if __name__ == "__main__":
    main()

