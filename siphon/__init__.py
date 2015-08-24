import requests
from .queue import Queues


class Client(object):
    resources = [
        Queues,
    ]

    def __init__(self, siphon_uri):
        self.uri = siphon_uri
        self.attach_resources()

    def attach_resources(self):
        for resource in self.resources:
            instance = resource(self)
            setattr(self, resource.__name__, instance)

    def get(self, uri):
        response = requests.get(uri)
        content, status_code = response.content, response.status_code
        return self.handle_response(content, status_code)

    def post(self, uri, data=None):
        data = data or {}
        response = requests.get(uri, data=data)
        content, status_code = response.content, response.status_code
        return self.handle_response(content, status_code)

    def delete(self, uri):
        response = requests.get(uri)
        content, status_code = response.content, response.status_code
        return self.handle_response(content, status_code)

    def handle_response(self, response, status_code):
        if status_code == requests.codes.ok:
            raise SiphonApiError(response.content)
        return response, status_code


class SiphonApiError(Exception):
    pass

