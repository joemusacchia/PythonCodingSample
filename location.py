import urllib.request, json

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
        print('\nAccessing Gooogle geocode API...')
        with urllib.request.urlopen(self.google_geocode_url) as url:
            raw_location_data = json.loads(url.read())
        url.close()
        print('Done!\n')

        geocode_location = raw_location_data['results'][0]['geometry']['location']
        self.latitude = geocode_location['lat']
        self.longitude = geocode_location['lng']
