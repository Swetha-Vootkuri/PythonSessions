import requests

def get_json_output_dict(url):
    url = "http://192.168.0.215:9006/as/services"
    r = requests.get(url)
    output = r.json()
    return output

def get_all_services():
    output = get_json_output_dict(url = "url")
    services_dict = output["services"]
    return services_dict

def get_all_hd_channels():
    output = get_all_services()
    hd_channels = []
    for item in output:
        if item["sf"] == "hd":
         hd_channels.append(item["t"])
    return hd_channels

def get_channel_by_type(sf = None):
    output = get_all_services()
    channel_list = []
    for channel in output:
        if channel["sf"] == "hd":
         channel_list.append(channel["t"])
    return channel_list

if __name__ == "__main__":
    output = get_json_output_dict(url = "url")
    #print(output)
    #print(get_all_services())
    #print(get_all_hd_channels())
    print(len(get_all_hd_channels()))
    #print(get_channel_by_type(sf= "hd"))
    hd_channel_count = get_channel_by_type(sf="hd")
    print(len(hd_channel_count))
