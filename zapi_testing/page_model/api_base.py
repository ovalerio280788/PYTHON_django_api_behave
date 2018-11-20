import urllib3


class ApiBase:

    def __init__(self, context):
        self.context = context
        urllib3.disable_warnings()

    @property
    def url(self):
        return self.context.config.userdata.get('base_api_url')
