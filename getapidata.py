import urllib.request, json

class Getapidata:
    def __init__(self, url, message):
        self.url = url
        self.message = message

    def get_data_from_api(self):
        print(self.message)
        with urllib.request.urlopen(self.url) as response:
            raw_api_data = json.loads(response.read())
        print('Done!\n')
        return raw_api_data
