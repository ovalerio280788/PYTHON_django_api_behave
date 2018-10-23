import requests

from zapi_testing.page_model.api_base import ApiBase


class Home(ApiBase):
    HOMES_BASE_URL = 'api/homes/'

    @property
    def all_homes(self):
        response = requests.get("{}{}".format(self.url, self.HOMES_BASE_URL), auth=self.auth, verify=False)
        return response.json(), response.status_code
