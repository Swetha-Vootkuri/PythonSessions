#Get as version of a dictionary "http://192.168.0.215:9006/as/system/information"

import requests
def get_json_output_dict(url):
    r = requests.get(url)
    output = r.json()
    return output


'''def get_as_version():
    output = get_json_output_dict(url ="http://192.168.0.215:9006/as/system/information")
    key = output.get("ASVersion")
    return key
    
if __name__ == "__main__":
   output = get_as_version()
   print(output)'''

#or
def get_as_version(key = None):
    output = get_json_output_dict(url ="http://192.168.0.215:9006/as/system/information")
    if key is not None:
        return output[key]
    return output

def get_system_smartcard_details():
    url = "http://192.168.0.215:9006/as/system/smartcard"
    smartcard_details = get_json_output_dict(url)
    #return smartcard_details # returns whole dictionary
    return smartcard_details["smartcard"] #returns only smartcard key values



if __name__ == "__main__":
   output = get_as_version(key = "ASVersion")
   print(output)
   output = get_system_smartcard_details()
   print(output)


'''#Check Drmactivestatus is active

def get_drm_status():
    output = get_json_output_dict(url = "http://192.168.0.215:9006/as/system/information" )
    if "DRMActivationStatus" in output.keys() and output["DRMActivationStatus"]:
        key = output.get("DRMActivationStatus")
        return key


if __name__ == "__main__":
   url = "http://192.168.0.215:9006/as/system/information" 
   output = get_drm_status()
   print(output)
'''