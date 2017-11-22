import pdb
from google_maps_api_key import API_KEY
from location import Location
from elevation import Elevation
from weather import Weather
from job import Job

print('\nThis python script displays information about a user provided address\n')
address = input('Number and street name: ')
city = input('Name of city/town: ')
state = input('State: ')

# instantiate a new Location object
new_location = Location(address, city, state, API_KEY)

# convert address to geocode using class methods
new_location.get_geocode_from_address()

# instantiate a new Elevation object
new_elevation = Elevation(new_location)

# get elevation data
new_elevation.get_elevation_data()

# instantiate new Weather object
new_weather = Weather(new_location)

# get current forecast
new_weather.get_weather_right_now()

#instantiate new Job object
new_job = Job(new_location)

# get raw jobs data
new_job.get_github_jobs_data()

##### Print out all requested information:

print(f'\n\n\nElevation, forecast, and dev jobs for {new_location.pretty_print_address}:\n')

print(f'Elevation:\n{round(new_elevation.elevation, 4)} meters above sea level\nWith a resolution of: {round(new_elevation.resolution, 4)} meters\n')

print(f'Forecast right now:\n{new_weather.forecast}\n')

print('Current job openings on Github:\n')

if len(new_job.raw_github_jobs_data) != 0:
    for job in new_job.raw_github_jobs_data:
        job_posted_at = job['created_at']
        print(f'Job posted at: {job_posted_at}')
        job_title = job['title']
        print(f'Title: {job_title}')
        job_company = job['company']
        print(f'Company: {job_company}\n')
else:
    print('There are no jobs recently posted in your area.\n')
