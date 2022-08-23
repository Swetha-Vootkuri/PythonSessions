#Weather by lat, long

#Find lat,long from map and iput
import requests

def get_json_output(url):
    r = requests.get(url)
    output = r.json()
    return output

def get_weather_lat_long_by_location(location = None):
    url = f"https://www.metaweather.com/api/location/search/?query={location}"
    output = get_json_output(url = url)
    




