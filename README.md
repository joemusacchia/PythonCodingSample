# README

## Python coding sample for accessing json data on the web

I wrote a python script to access data from API endpoints on the web.  The user provides an address, a city, and a state at the command prompt.  The script use the Google Maps Geocoding API to convert the address into lat and long coordinates.  The coordinates are then used to find elevation from the Google Maps Elevation API, the location's current forecast from the National Weather Service, and the latest job openings posted to Github jobs (if available).

This most current version (ver 2) attempts to add OOP to this script.

## Technology and setup

This script uses Python3.6, so you will need to have that installed.  You can do so on Mac OSX via:
```
$ brew install python3
```
To run the script, clone down this repo and then execute in the terminal from the repo's root directory:
```
$ python3.6 access_json_data.py
```
Be sure to use `Python3.X` since the formatted string interpolation syntax (e.g. `f'Hi my name is {my_name_var}'`) is specific to `Python3.X`.

#### NOTE ON SETUP:

Since the Google Maps APIs are private, you need to generate an API key to access their APIs.  The `google_maps_api_key.py` file containing my personal API key was not included in this repo for security reasons. You can create your own using the [google api console](https://console.developers.google.com/apis/). Create a new project for this API key, and be sure to enable both the geocoding API and the elevation API.  Create your own `google_maps_api_key.py` with contents:
```
API_KEY = 'your_key_here'
```

#### NOTE ON TECHNOLOGY:

I utilized `urllib.request` with the `urlopen()` method to access the API endpoint using `with...as url:`.  I then convert the returned `url` HTTP response as a json object/python dictionary.  At each raw data return, I used the `pdb.set_trace()` debugger statement to investigate the returned data to manually extract the desired values.
