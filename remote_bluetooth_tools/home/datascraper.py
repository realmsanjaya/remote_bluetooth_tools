import requests
import json

# Purpose to create a scraper

class Scraper:
    def __init__(self):
        self.cveid = 'CVE-2021-3573'
        self.cve_url = 'https://services.nvd.nist.gov/rest/json/cve/1.0/'
        self.cves_url ='https://services.nvd.nist.gov/rest/json/cves/1.0?keyword=bluetooth'
        self.cve_vulnerability_detail = 'https://services.nvd.nist.gov/rest/json/cve/1.0/'

        """
        https://services.nvd.nist.gov/rest/json/cve/1.0/CVE-2021-31612
        """

    def statement(self):
        """ Prints out a statement """
        return f"Lookup for: {self.cveid}"

    def get_cve_details(self):
        """ Return a JSON value """
        url = f"{self.cve_url}{self.cveid}"
        data = requests.get(url)
        return data.json()

    def get_cves_details(self):
        """ Returns a JSON value for Bluetooth Vulnerabilities """
        cve_list = []
        url = self.cves_url
        data = requests.get(url)
        results = dict(data.json())
        for result in results['result']['CVE_Items']:
            cve_id = result['cve']['CVE_data_meta']['ID']
            cve_description = result['cve']['description']['description_data'][0]['value']
            data = {'cve_id':cve_id, 'cve_description':cve_description}
            cve_list.append(data)
        return cve_list
        
    def vulnerability_detail(self, cveid):
        """ Pull details of a vulnerability. Return data in JSON """
        url = f"{self.cve_vulnerability_detail}{cveid}"
        data = requests.get(url)
        return json.loads(data.text)


if __name__ =='__main__':
    data = Scraper()
    #print(data.get_cves_details())
    print(data.vulnerability_detail(cveid='CVE-2021-31612'))