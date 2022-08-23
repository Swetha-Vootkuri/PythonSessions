import requests

'''def get_json_output_dict(url):
    r = requests.get(url)
    output = r.json()
    return output

if __name__ == "__main__":
   url = "http://192.168.0.215:9006/as/system/information"
   output = get_json_output_dict(url)
   print(output)

# or
def get_json_output_dict(url= None):
    r = requests.get(url)
    output = r.json()
    return output

if __name__ == "__main__":
   output = get_json_output_dict(url = "http://192.168.0.215:9006/as/system/information")
   print(output)
   

#or
def get_json_output_dict(url="http://192.168.0.215:9006/as/system/information" ):
    r = requests.get(url)
    output = r.json()
    return output

if __name__ == "__main__":
   output = get_json_output_dict()
   print(output)
   '''
#or
'''def get_json_output_dict(url):
    r = requests.get(url)
    output = r.json()
    return output

if __name__ == "__main__":
    ipaddress = "192.168.0.215"
    port = "9006"
    url = f"http://{ipaddress}:{port}/as/system/information"
    output = get_json_output_dict(url = url)
    print(output)'''

#or
'''def get_json_output_dict(ipaddress, port, api ):
    ipaddress = "192.168.0.215"
    port = "9006"
    api = "as/system/information"
    url = f"http://{ipaddress}:{port}/{api}"
    r = requests.get(url)
    output = r.json()
    return output

if __name__ == "__main__":
    output = get_json_output_dict(ipaddress = "ipaddress", port ="port", api= "api")
    print(output)
'''



