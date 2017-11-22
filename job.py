import urllib.request, json

class Job:
    def __init__(self, location_object):
        self.location_object = location_object
        self.raw_github_jobs_data = []

        latitude = self.location_object.latitude
        longitude = self.location_object.longitude
        self.github_jobs_url = f'https://jobs.github.com/positions.json?lat={latitude}&long={longitude}'

    def get_github_jobs_data(self):
        print('Finding recent jobs in your area on Github jobs...')
        with urllib.request.urlopen(self.github_jobs_url) as url:
            self.raw_github_jobs_data = json.loads(url.read())
        print('Done!\n')
