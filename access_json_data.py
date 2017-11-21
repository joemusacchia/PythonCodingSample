# urllib.request is python3 specific; python2 is simply urllib
import pdb, urllib.request, urllib.error, json, contextlib
from google_maps_api_key import API_KEY

print("This python script displays information about a user provided address")
address = input('Number and street name: ')
city = input('Name of city/town: ')
state = input('State: ')

address_string = f'{address.replace(" ", "+")},+' + f'{city.replace(" ", "+")},+' + f'{state.replace(" ", "+")}'

google_geocode_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address_string}&key={API_KEY}'

pdb.set_trace()

with urllib.request.urlopen(google_geocode_url) as url:
    raw_location_data = json.loads(url.read())
    print(raw_location_data)
url.close()

geocode_location = raw_location_data['results'][0]['geometry']['location']
latitude = geocode_location['lat']
longitude = geocode_location['lng']

google_elevation_url = f'https://maps.googleapis.com/maps/api/elevation/json?locations={latitude},{longitude}&key={API_KEY}'

with urllib.request.urlopen(google_elevation_url) as url:
    raw_elevation_data = json.loads(url.read())
    print(raw_elevation_data)
url.close()

actual_elevation = raw_elevation_data['results'][0]['elevation']
national_weather_service_url = f'https://api.weather.gov/points/{round(latitude, 4)},{round(longitude, 4)}/forecast'
print(national_weather_service_url)

# I had figured out via curl that the headers this server required weren't working with the implicit method so I had to create another request object containing the header and pass that into urlopen()
req = urllib.request.Request(national_weather_service_url, headers={'Accept': '*/*'} )

with urllib.request.urlopen(req) as url:
    #pdb.set_trace()
    raw_weather_data = json.loads(url.read())
    print(raw_weather_data)
url.close()


weather_right_now = raw_weather_data['properties']['periods'][0]['detailedForecast']

pdb.set_trace()
