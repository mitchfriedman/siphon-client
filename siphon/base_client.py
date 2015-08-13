import requests


class BaseClient(object):

    def __init__(self, siphon_url):
        self.url = siphon_url

    def get(self, path):
        response = make_request("GET", path)

    def post(self, path, data=None):
        response = make_request("POST", path, data=data)


def make_request(method, url, data=None):
    if method.upper() == 'GET':
        return requests.get(url)
    elif method.upper() == 'POST':
        return requests.post(url, data or {})

