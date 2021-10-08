import requests
import json
from .models import CVETable

# Purpose to create a scraper

class Scraper:
    def __init__(self):
        self.cves_url ='https://services.nvd.nist.gov/rest/json/cves/1.0?keyword=bluetooth'
        self.cve_vulnerability_detail = 'https://services.nvd.nist.gov/rest/json/cve/1.0/'

        """
        https://services.nvd.nist.gov/rest/json/cve/1.0/CVE-2021-31612
        """

    def pull_cve_bluetooth(self):
        """ Pulls all of the bluetooth CVE """
        cve_list = []
        url = self.cves_url
        r = requests.get(url)
        results = dict(r.json())
        # Build dictionary
        for result in results['result']['CVE_Items']:
            cve_id = result['cve']['CVE_data_meta']['ID']
            cve_description = result['cve']['description']['description_data'][0]['value']
            cve_json = result
            data = CVETable(cve_id=cve_id, cve_description=cve_description, data=cve_json)
            data.save()

if __name__=="__main__":
    db_pull = Scraper()
    db_pull.pull_cve_bluetooth()