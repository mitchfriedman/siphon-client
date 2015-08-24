import unittest
from mock import patch
from siphon import Client
from siphon.queue import Queues as QueuesClass


class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = Client('http://localhost:8000/api')

    def test_create_client(self):
        self.assertEqual('http://localhost:8000/api', self.client.uri)

    @patch('siphon.Client.get')
    def test_get_request(self, request):
        response, status_code = {
            'id': 'foo',
            'type': 'email',
            'creator': 'mitch'
        }, 200
        request.return_value = response, status_code
        resp, status_code = self.client.get('/foo123/Dequeue')
        self.assertEqual(response, resp)
        self.assertEqual(200, status_code)
        request.assert_called_with('/foo123/Dequeue')

    @patch('siphon.Client.post')
    def test_post_request(self, request):
        response, status_code = {
            'id': 'foo',
            'type': 'email',
            'creator': 'mitch'
        }, 201

        request.return_value = response, status_code
        resp, status_code = self.client.post('/foo123/Dequeue')
        self.assertEqual(201, status_code)
        self.assertEqual(response, resp)
        request.assert_called_with('/foo123/Dequeue')

    def test_attach_resources(self):
        Queues = self.client.Queues

        self.assertTrue(isinstance(Queues, QueuesClass))
