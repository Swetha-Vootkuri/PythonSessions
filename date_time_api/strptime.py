#syntax of strptime()  datetime.strptime(date_string,format)
#This function changes the given string of datetime into the desired format.
#The arguments date_string and format should be of string type

## Function to convert string to datetime

import datetime

def convert(date_string):
     format = "%b %d %Y %I:%M%p"
     datetime_string = datetime.datetime.strptime(date_string,format)
     return datetime_string


date_string = "Dec 4 2018 10:07AM"
print(convert(date_string))
'''

if __name__ == '__main__':
    conversion = convert("Dec 4 2018 10:07AM")
    print(conversion)'''


#convert DateTime to string using time.strftime
#syntax of strftime()  datetime_object.strftime(format_str)

import time
def convert(datetime_str):
    datetime_str = time.mktime(datetime_str)

    format = "%b %d %Y %r"  # The format
    dateTime = time.strftime(format, time.gmtime(datetime_str))
    return dateTime


# Driver code
datetime_str = (2018, 12, 4, 10, 7, 00, 1, 48, 0)
print(convert(datetime_str))
