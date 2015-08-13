import unittest
from mock import patch
from siphon.base_client import BaseClient


class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = BaseClient('http://localhost:8000')

    def test_create_client(self):
        self.assertEqual('http://localhost:8000', self.client.url)

    @patch('siphon.base_client.make_request')
    def test_get_request(self, request):
        response = {
            'id': 'foo',
            'type': 'email',
            'creator': 'mitch'
        }
        request.return_value = response
        resp = self.client.get('/dequeue/foo123')
        self.assertEqual(response, resp)
        request.assert_called_with('GET', '/dequeue/foo123')

    @patch('siphon.base_client.make_request')
    def test_post_request(self, request):
        response = {
            'id': 'foo',
            'type': 'email',
            'creator': 'mitch'
        }

        request.return_value = response
        resp = self.client.post('/dequeue/foo123')
        self.assertEqual(response, resp)
        request.assert_called_with('POST', '/dequeue/foo123', data=None)
