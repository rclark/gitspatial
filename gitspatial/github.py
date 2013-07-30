import json

import requests
from social_auth.models import UserSocialAuth


class GitHubApiRequest(object):
    _base_uri = 'https://api.github.com'

    def __init__(self, user=None, method=None, payload=None):
        self._user = user
        self._method = method
        self._uri = self._base_uri + self._method

        social_auth_user = UserSocialAuth.objects.get(user=user, provider='github')
        social_extra = social_auth_user.extra_data
        access_token = social_extra['access_token']
        self._headers = {'Authorization': 'token {0}'.format(access_token)}


class GitHubApiGetRequest(GitHubApiRequest):
    def __init__(self, user, method):
        super(GitHubApiGetRequest, self).__init__(user=user, method=method)

        request = requests.get(self._uri, headers=self._headers)
        self.status_code = request.status_code
        self.json = request.json()


class GitHubApiPostRequest(GitHubApiRequest):
    def __init__(self, user, method, payload):
        super(GitHubApiPostRequest, self).__init__(user=user, method=method, payload=payload)

        request = requests.post(self._uri, headers=self._headers, data=json.dumps(payload))
        self.status_code = request.status_code
        self.json = request.json()

"""
def github_api_request(user, method, verb='GET'):
    social_auth_user = UserSocialAuth.objects.get(user=user, provider='github')
    social_extra = social_auth_user.extra_data
    access_token = social_extra['access_token']

    uri = 'https://api.github.com{0}'.format(method)
    headers = {'Authorization': 'token {0}'.format(access_token)}
    request = requests.get(uri, headers=headers)

    return request.json()
"""