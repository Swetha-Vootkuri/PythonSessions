
#1.Write a function to return all ITV channels sids


import requests

def get_output_dict(url):
    r = requests.get(url)
    if r.status_code == 200:
        output_dict = r.json()
        return output_dict
    else:
        print("Error")

def get_all_itv_channel_sids(output_dict):
    itv_channel_names=[]
    services_list = output_dict["services"]
    for service in services_list:
        if service["t"].startswith("ITV"):
            itv_channel_names.append(service["sid"])
    return itv_channel_names

def main():
    url = "http://192.168.0.215:9006/as/services"
    output_dict = get_output_dict(url)
    itv_channel_sids = get_all_itv_channel_sids(output_dict)
    print(itv_channel_sids)

if __name__ == "__main__":
    main()

