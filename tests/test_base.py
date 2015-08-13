import unittest
from mock import patch, Mock
import siphon
from siphon.base_resource import ListResource, InstanceResource
from siphon.base_client import BaseClient


class TestListResource(unittest.TestCase):

    def setUp(self):
        client = BaseClient('http://localhost:8000')
        self.resource = ListResource(client)

    def test_create_list_resource(self):
        self.assertEqual('ListResource', self.resource.name)
        self.assertEqual('list_resource', self.resource.response_key)
    
    @patch('siphon.base_client.BaseClient.get')
    def test_get_instance(self, request):
        response, status_code = {
            'id': 'foo'
        }, 200
        request.return_value = response, status_code
        instance = self.resource.get_instance('foo')
        self.assertEqual('foo', instance.id)
        self.assertEqual({}, instance.data)

