import urllib3
from requests.auth import HTTPBasicAuth


class ApiBase:

    def __init__(self, context, username, password):
        self.username = username
        self.password = password
        self.context = context
        self.auth = HTTPBasicAuth(self.username, self.password)
        urllib3.disable_warnings()

    @property
    def url(self):
        return self.context.config.userdata.get('base_api_url')
