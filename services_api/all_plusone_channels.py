#4.Write a function to return all the +1 channels(title names)(time shifted = true)

import requests

def get_output_dict(url):
    r = requests.get(url)
    if r.status_code == 200:
        output_dict = r.json()
        return output_dict
    else:
        print("Error")

def get_all_plusone_channel_names(output_dict):
    all_plusone_channel_names=[]
    plusone_channel_names = output_dict["services"]
    for service in plusone_channel_names:
        #if service["t"].endswith("+1") :
        if "timeshifted" in service.keys() and service["timeshifted"]:
            all_plusone_channel_names.append(service["t"])
    return all_plusone_channel_names


def main():
    url = "http://192.168.0.215:9006/as/services"
    output_dict = get_output_dict(url)
    all_plus_one_channel_names = get_all_plusone_channel_names(output_dict)
    print(all_plus_one_channel_names)


if __name__ == "__main__":
    main()

