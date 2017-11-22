from getapidata import Getapidata

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
        api_data_obj = Getapidata(self.google_elevation_url,'Getting elevation from Google elevation API...')
        raw_elevation_data = api_data_obj.get_data_from_api()

        self.elevation = raw_elevation_data['results'][0]['elevation']
        self.resolution = raw_elevation_data['results'][0]['resolution']
