import requests

def get_json_output_dict(url):
    r = requests.get(url)
    output = r.json()
    return output

def get_all_appids():
    output = get_json_output_dict(url = "http://192.168.0.215:9006/as/apps")
    app_ids = []
    print(dir(list))
    result = output["apps"]
    for item in result:
        print(type(item))
        app_ids.append(item["appId"]) #returns all appids of apps dict
    return app_ids

def get_all_sky_appids():
    sky_appids = get_all_appids()
    sky_all_appids = []
    for appid in sky_appids:
        if appid.startswith("com.bskyb"):
            sky_all_appids.append(appid)
    return sky_all_appids


if __name__ == "__main__":
    output = get_json_output_dict(url = "http://192.168.0.215:9006/as/apps")
    #print(output)
    result_appids = get_all_appids()
    print(result_appids)
    '''sky_app_ids = get_all_sky_appids()
    print(sky_app_ids)'''
    print(get_all_sky_appids())