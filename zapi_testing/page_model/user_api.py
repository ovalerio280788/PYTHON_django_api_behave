import requests

from zapi_testing.page_model.api_base import ApiBase


class Users(ApiBase):
    USERS_BASE_URL = 'api/users/'

    @property
    def all_users(self):
        response = requests.get("{}{}".format(self.url, self.USERS_BASE_URL), auth=self.auth, verify=False)
        return response.json(), response.status_code

    def create_user(self, username, email):
        body = dict()
        body['username'] = username
        body['email'] = email
        response = requests.post("{}{}".format(self.url, self.USERS_BASE_URL), json=body, auth=self.auth, verify=False)
        return response.json(), response.status_code

    def delete_user(self, user_id):
        response = requests.delete("{}{}{}".format(self.url, self.USERS_BASE_URL, "{}/".format(user_id)), auth=self.auth)
        return response.status_code

    def update_user(self, user_id=None, username=None, email=None):
        body = dict()
        if username:
            body['username'] = username

        if email:
            body['email'] = email

        response = requests.put("{}{}{}".format(self.url, self.USERS_BASE_URL, "{}/".format(user_id)), json=body, auth=self.auth,
                                verify=False)
        return response.json(), response.status_code
