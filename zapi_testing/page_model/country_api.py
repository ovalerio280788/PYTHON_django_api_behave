import requests

from zapi_testing.page_model.api_base import ApiBase


class Countries(ApiBase):
    COUNTRIES_BASE_URL = 'country/'

    @property
    def all_countries(self):
        response = requests.get("{}{}".format(self.url, self.COUNTRIES_BASE_URL + "get/all"), verify=False)
        return response.json(), response.status_code

    def single_country(self, expected_country):
        response = requests.get("{}{}{}".format(self.url, self.COUNTRIES_BASE_URL + "get/iso2code/", expected_country), verify=False)
        return response.json(), response.status_code

    def create_country(self, name, alpha2, alpha3):
        body = dict()
        body['name'] = name
        body['alpha2_code'] = alpha2
        body['alpha3_code'] = alpha3
        response = requests.post("{}{}".format(self.url, self.COUNTRIES_BASE_URL + "add"), json=body, verify=False)
        return response.status_code
