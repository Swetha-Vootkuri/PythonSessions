import requests

def get_output_dict(url):
    r = requests.get(url)
    if r.status_code == 200:
        output_dict = r.json()
        return output_dict
    else:
        print("Error")

def get_all_entitlements(output_dict):
    entitlements = output_dict["entitlements"]["ids"]
    state = output_dict["entitlements"]["state"].split(",")
    print(state)
    return entitlements


def main():
    url = "http://192.168.0.181:9006/as/system/entitlements"
    output_dict = get_output_dict(url)
    entitlements_item_list = get_all_entitlements(output_dict)
    print(entitlements_item_list)

if __name__ == "__main__":
    main()