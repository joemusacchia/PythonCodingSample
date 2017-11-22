from getapidata import Getapidata

class Job:
    def __init__(self, location_object):
        self.location_object = location_object
        self.raw_github_jobs_data = []

        latitude = self.location_object.latitude
        longitude = self.location_object.longitude
        self.github_jobs_url = f'https://jobs.github.com/positions.json?lat={latitude}&long={longitude}'

    def get_github_jobs_data(self):
        api_data_obj = Getapidata(self.github_jobs_url,'Finding recent jobs in your area on Github jobs...')
        self.raw_github_jobs_data = api_data_obj.get_data_from_api()
