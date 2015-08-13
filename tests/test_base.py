import unittest
from mock import patch, Mock
import siphon
from siphon.base_resource import ListResource, InstanceResource


class TestListResource(unittest.TestCase):

    def setUp(self):
        client = Mock()
        self.resource = ListResource(client)

    def test_create_list_resource(self):
        self.assertEqual('ListResource', self.resource.name)
        self.assertEqual('list_resource', self.resource.response_key)

    def test_get_instance(self):
        instance = self.resource.get_instance('1')
        self.assertEqual('1', instance.id)
        self.assertEqual({}, instance.data)
    


