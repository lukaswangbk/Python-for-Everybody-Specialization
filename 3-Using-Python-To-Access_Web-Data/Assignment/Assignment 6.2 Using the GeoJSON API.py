"""Calling a JSON API"""

'''
In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

API End Points

To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:

http://py4e-data.dr-chuck.net/geojson?
This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get a list of all of the address values which can be used with this API.
To call the API, you need to provide address that you are requesting as the address= parameter that is properly URL encoded using the urllib.urlencode() fuction as shown in http://www.py4e.com/code3/geojson.py

Make sure to check that your code is using the API endpoint is as shown above. You will get different results from the geojson and json endpoints so make sure you are using the same end point as this autograder is using.

Test Data / Sample Execution

You can test to see if your program is working with a location of "South Federal University" which will have a place_id of "ChIJJ2MNmPl_bIcRt8t5x-X5ZhQ".
$ python3 solution.py
Enter location: South Federal University
Retrieving http://...
Retrieved 2290 characters
Place id ChIJJ2MNmPl_bIcRt8t5x-X5ZhQ

Turn In

Please run your program to find the place_id for this location:

Obninsk Technical University of Nuclear Power Engineering Russia
Make sure to enter the name and case exactly as above and enter the place_id and your Python code below. Hint: The first seven characters of the place_id are "ChIJw7x ..."
Make sure to retreive the data from the URL specified above and not the normal Google API. Your program should work with the Google API - but the place_id may not match for this assignment.
'''

#Enter location: Obninsk Technical University of Nuclear Power Engineering Russia
#Retrieving http://python-data.dr-chuck.net/geojson?sensor=false&address=Obninsk+Technical+University+of+Nuclear+Power+Engineering+Russia
#Retrieved 1770 characters
#Place id ChIJ98gRfsDSykYRrQirpg0x418



import urllib.request as ur
import urllib.parse as up
import json

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

address_input = input("Enter location: ")
params = dict()
params['address'] = address_input
if api_key is not False: params['key'] = api_key

url = serviceurl + up.urlencode(params)
print("Retrieving", url)
data = ur.urlopen(url).read().decode()
print('Retrieved', len(data), 'characters')
json_obj = json.loads(data)

place_id = json_obj["results"][0]["place_id"]
print("Place id", place_id)