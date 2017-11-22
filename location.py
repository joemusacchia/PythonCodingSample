from getapidata import Getapidata

class Location:
    def __init__(self, address, city, state, api_key):
        self.address = address
        self.city = city
        self.state = state
        self.api_key = api_key
        self.latitude = ''
        self.longitude = ''

        address_string = f'{self.address.replace(" ", "+")},+' + f'{self.city.replace(" ", "+")},+' + f'{self.state.replace(" ", "+")}'
        self.google_geocode_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address_string}&key={self.api_key}'
        self.pretty_print_address = self.pretty_print_address = f'{self.address}, {self.city}, {self.state}'

    def get_geocode_from_address(self):
        api_data_obj = Getapidata(self.google_geocode_url,'\nAccessing Gooogle geocode API...')
        raw_location_data = api_data_obj.get_data_from_api()
        geocode_location = raw_location_data['results'][0]['geometry']['location']
        self.latitude = geocode_location['lat']
        self.longitude = geocode_location['lng']
