import requests
# Purpose to create a scraper

class Scraper:
    def __init__(self, cveid):
        self.cveid = cveid
        self.cve_url = 'https://services.nvd.nist.gov/rest/json/cve/1.0/'

    def statement(self):
        """ Prints out a statement """
        return f"Lookup for: {self.cveid}"

    def get_cve_details(self):
        """ Return a JSON value """
        url = f"{self.cve_url}{self.cveid}"
        data = requests.get(url)
        return data.json()