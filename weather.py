import urllib.request, json

class Weather:
    def __init__(self, location_object):
        self.location_object = location_object
        self.forecast = ''

        latitude = self.location_object.latitude
        longitude = self.location_object.longitude
        self.national_weather_service_url = f'https://api.weather.gov/points/{round(latitude, 4)},{round(longitude, 4)}/forecast'

    def get_weather_right_now(self):
        # I had figured out via curl that the headers this server required weren't working with the implicit method so I had to create another request object containing the header and pass that into urlopen()
        req = urllib.request.Request(self.national_weather_service_url, headers={'Accept': '*/*'} )

        print('Getting current weather from National Weather Service...')
        with urllib.request.urlopen(req) as url:
            raw_weather_data = json.loads(url.read())
        url.close()
        print('Done!\n')

        self.forecast = raw_weather_data['properties']['periods'][0]['detailedForecast']
