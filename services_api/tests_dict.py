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
    print(output_dict.keys())
    services_list = output_dict["services"]
    for service in services_list:
        print(service["t"])
        channel_names.append(service["t"])
    print(services_list)
    return channel_names

def get_all_channel_numbers(output_dict):
    channel_numbers = []
    services = output_dict["services"]
    for service_dict in services:
        channel_number = service_dict["c"]
        print(channel_number)
        channel_numbers.append(channel_number)
    return channel_numbers

def get_all_hd_channel_names(output_dict):
    hd_channel_names = []
    services = output_dict["services"]
    for service in services:
        if service["sf"] == "hd":
            hd_channel_names.append(service["t"])
    return hd_channel_names

def get_all_sky_channel_names(output_dict):
    all_sky_channels = []
    services = output_dict["services"]
    for service in services:
        if service["t"].startswith("Sky"):
            all_sky_channels.append(service["t"])

    return all_sky_channels
def main():
    url = "http://192.168.0.215:9006/as/services"
    output_dict = get_output_dict(url)
    channelnames = get_all_channel_names(output_dict)
    print(channelnames)
    all_channel_numbers = get_all_channel_numbers(output_dict)
    print(all_channel_numbers)
    hd_channels = get_all_hd_channel_names(output_dict)
    print(hd_channels)
    sky_channels = get_all_sky_channel_names(output_dict)
    print(sky_channels)


if __name__ == "__main__":
    main()

