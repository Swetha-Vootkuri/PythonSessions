import requests

def get_json_output_dict(url):
    r = requests.get(url)
    output = r.json()
    return output

def get_all_genres():
    genres_output = get_json_output_dict(url = "http://192.168.0.215:9006/as/services/genres")
    genres_items = genres_output["genres"]
    return genres_items

def get_genre_by_name(genre_title = None):
    genre_output = get_all_genres()
    for genre in genre_output:
        if genre["t"] == "Movies":
          return genre["sg"]

def get_all_channel_by_genre(genre = None):
    output = get_json_output_dict(url="http://192.168.0.215:9006/as/services")
    services_dict = output["services"]
    channel_list = []
    for channel in services_dict:
        if channel["sg"] == 14:
            channel_list.append(channel["t"])
    return channel_list

if __name__ == "__main__":
   genre_sg = get_genre_by_name(genre_title= "Movies")
   print(genre_sg)
   movie_channels = get_all_channel_by_genre(genre = genre_sg)
   print(movie_channels)

