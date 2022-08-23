import requests

def get_output_dict(url):
    r = requests.get(url)
    if r.status_code == 200:
        output_dict = r.json()
    return output_dict

def get_all_vod_asset_titles(output_dict):
    vod_assets = output_dict["pvrItems"]
    for asset in vod_assets:
        if "VOD" in asset.values():
        #if asset["src"] == "VOD":
            vod_assets.append(asset["t"])
    return vod_assets

def main():
    url = "http://192.168.0.215:9006/as/pvr?offset=0&limit=1000"
    output_dict = get_output_dict(url)
    vod_assets_titles = get_all_vod_asset_titles(output_dict)
    print(vod_assets_titles)


if __name__ == "__main__":
    main()