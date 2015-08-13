import unittest
import client
from client.base_resource import Resource


class TestResource(unittest.TestCase):

    def test_create_resource(self):
        resource = Resource()
        self.assertEqual(resource.base_uri, client.api_base)
        self.assertEqual(resource.name, "Resource")
        self.assertEqual(resource.response_key, "resource")


