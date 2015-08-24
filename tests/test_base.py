import unittest
from mock import patch
from siphon.base_resource import ListResource
from siphon import Client


class TestListResource(unittest.TestCase):

    def setUp(self):
        client = Client('http://localhost:8000')
        self.resource = ListResource(client)

    def test_create_list_resource(self):
        self.assertEqual(None, self.resource.uri_name)
        self.assertEqual(None, self.resource.response_key)
    
    @patch('siphon.Client.get')
    def test_get_instance(self, request):
        response, status_code = {
            'name': 'foo'
        }, 200
        request.return_value = response, status_code
        instance = self.resource.get_instance('foo')
        self.assertEqual('foo', instance.name)
        self.assertEqual({}, instance.data)
