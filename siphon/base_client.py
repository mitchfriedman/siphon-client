import requests


class BaseClient(object):

    def __init__(self, siphon_url):
        self.url = siphon_url

    def get(self, uri):
        response = requests.get(uri)
        content, status_code = response.content, response.status_code
        return self.handle_response(content, status_code)

    def post(self, uri, data=None):
        data = data or {}
        response = requests.get(uriuri, data=data)
        content, status_code = response.content, response.status_code
        return self.handle_response(content, status_code)

    def handle_response(self, response, status_code):
        if status_code == requests.codes.ok:
            raise SiphonApiError(response.content)
        return response, status_code


class SiphonApiError(Exception):
    pass

