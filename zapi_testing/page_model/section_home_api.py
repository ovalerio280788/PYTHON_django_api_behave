import requests

from zapi_testing.page_model.api_base import ApiBase


class SectionHome(ApiBase):
    SECTION_HOMES_BASE_URL = 'api/home/sections/'

    @property
    def all_section_homes(self):
        response = requests.get("{}{}".format(self.url, self.SECTION_HOMES_BASE_URL), auth=self.auth, verify=False)
        return response.json(), response.status_code
