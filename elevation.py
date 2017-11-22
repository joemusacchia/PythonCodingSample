import urllib.request, json

class Elevation:
    def __init__(self, location_object):
        self.location_object = location_object
        self.elevation = ''
        self.resolution = ''

        latitude = self.location_object.latitude
        longitude = self.location_object.longitude
        api_key = self.location_object.api_key
        self.google_elevation_url = f'https://maps.googleapis.com/maps/api/elevation/json?locations={latitude},{longitude}&key={api_key}'

    def get_elevation_data(self):
        print('Getting elevation from Google elevation API...')
        with urllib.request.urlopen(self.google_elevation_url) as url:
            raw_elevation_data = json.loads(url.read())
        url.close()
        print('Done!\n')

        self.elevation = raw_elevation_data['results'][0]['elevation']
        self.resolution = raw_elevation_data['results'][0]['resolution']
