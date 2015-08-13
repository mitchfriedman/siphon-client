import unittest
from mock import patch
from siphon.base_client import BaseClient


class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = BaseClient('http://localhost:8000')

    def test_create_client(self):
        self.assertEqual('http://localhost:8000', self.client.url)

    @patch('siphon.base_client.BaseClient.get')
    def test_get_request(self, request):
        response, status_code = {
            'id': 'foo',
            'type': 'email',
            'creator': 'mitch'
        }, 200
        request.return_value = response, status_code
        resp, status_code = self.client.get('/dequeue/foo123')
        self.assertEqual(response, resp)
        self.assertEqual(200, status_code)
        request.assert_called_with('/dequeue/foo123')

    @patch('siphon.base_client.BaseClient.post')
    def test_post_request(self, request):
        response, status_code = {
            'id': 'foo',
            'type': 'email',
            'creator': 'mitch'
        }, 201

        request.return_value = response, status_code
        resp, status_code = self.client.post('/dequeue/foo123')
        self.assertEqual(201, status_code)
        self.assertEqual(response, resp)
        request.assert_called_with('/dequeue/foo123')

