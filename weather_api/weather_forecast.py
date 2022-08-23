import requests

def get_json_output_dict(url):
    r = requests.get(url)
    output = r.json()
    return output

def get_hyderabd_weather_id(city_title = None):
    weather_output = get_json_output_dict(url = f"https://www.metaweather.com/api/location/search/?query={city_title}")
    weather_list_woeid = weather_output[0]["woeid"] # list should consider item as index
    return weather_list_woeid

#second API TO GET HYD WEATHER on different dates for 7 days weather
def get_all_weather_forecast_by_city(id = None):
    output = get_json_output_dict(url = "https://www.metaweather.com/api/location/2295414/")
    weather_deatils = output["consolidated_weather"]
    weather_types = []
    for weather_detail in weather_deatils:
        weather_type = weather_detail["weather_state_name"]
        weather_types.append(weather_type)
    return weather_types

if __name__ == "__main__":
    weather_id = get_hyderabd_weather_id(city_title= "Hyderabad")
    #print(weather_id)
    #weather_id = get_hyderabd_weather_id(city_title="Osterley")
    weather_types = get_all_weather_forecast_by_city(id = weather_id)
    print(weather_types)


