# urllib.request is python3 specific; python2 is simply urllib
import pdb, urllib.request, urllib.error, json, contextlib
from google_maps_api_key import API_KEY

print('\nThis python script displays information about a user provided address\n')
address = input('Number and street name: ')
city = input('Name of city/town: ')
state = input('State: ')

address_string = f'{address.replace(" ", "+")},+' + f'{city.replace(" ", "+")},+' + f'{state.replace(" ", "+")}'
pretty_print_address = f'{address}, {city}, {state}'

google_geocode_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address_string}&key={API_KEY}'

print('\nAccessing Gooogle geocode API...')
with urllib.request.urlopen(google_geocode_url) as url:
    raw_location_data = json.loads(url.read())
url.close()
print('Done!\n')

geocode_location = raw_location_data['results'][0]['geometry']['location']
latitude = geocode_location['lat']
longitude = geocode_location['lng']

google_elevation_url = f'https://maps.googleapis.com/maps/api/elevation/json?locations={latitude},{longitude}&key={API_KEY}'

print('Getting elevation from Google elevation API...')
with urllib.request.urlopen(google_elevation_url) as url:
    raw_elevation_data = json.loads(url.read())
url.close()
print('Done!\n')

actual_elevation = raw_elevation_data['results'][0]['elevation']
elevation_resolution = raw_elevation_data['results'][0]['resolution']
national_weather_service_url = f'https://api.weather.gov/points/{round(latitude, 4)},{round(longitude, 4)}/forecast'

# I had figured out via curl that the headers this server required weren't working with the implicit method so I had to create another request object containing the header and pass that into urlopen()
req = urllib.request.Request(national_weather_service_url, headers={'Accept': '*/*'} )

print('Getting current weather from National Weather Service...')
with urllib.request.urlopen(req) as url:
    raw_weather_data = json.loads(url.read())
url.close()
print('Done!\n')


weather_right_now = raw_weather_data['properties']['periods'][0]['detailedForecast']

github_jobs_url = f'https://jobs.github.com/positions.json?lat={latitude}&long={longitude}'

print('Finding recent jobs in your area on Github jobs...')
with urllib.request.urlopen(github_jobs_url) as url:
    raw_github_jobs_data = json.loads(url.read())
print('Done!\n')

##### Print out all requested information:

print(f'\n\n\nElevation, forecast, and dev jobs for {pretty_print_address}:\n')

print(f'Elevation:\n{round(actual_elevation, 4)} meters above sea level\nWith a resolution of: {round(elevation_resolution, 4)} meters\n')

print(f'Forecast right now:\n{weather_right_now}\n')

print('Current job openings on Github:\n')

if len(raw_github_jobs_data) != 0:
    for job in raw_github_jobs_data:
        job_posted_at = job['created_at']
        print(f'Job posted at: {job_posted_at}')
        job_title = job['title']
        print(f'Title: {job_title}')
        job_company = job['company']
        print(f'Company: {job_company}\n')
else:
    print('There are no jobs recently posted in your area.\n')
