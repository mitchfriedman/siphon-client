import unittest
from mock import patch
from siphon import Client
from siphon.queue import Queue


class TestQueues(unittest.TestCase):
    def setUp(self):
        self.client = Client('http://localhost:8000/api')
        self.Queues = self.client.Queues

    @patch('siphon.Client.post')
    def test_create_queue(self, response):
        response.return_value = {
            'name': 'some_name'
        }, 201
        queue = self.Queues.create_instance('some_name')

        self.assertEqual('some_name', queue.name)

    @patch('siphon.Client.get')
    def test_fetch_queue(self, response):
        response.return_value = {
            'name': 'foo'
        }, 201
        fetched = self.Queues.get_instance('foo')
        self.assertIsNotNone(fetched)
        self.assertEqual('foo', fetched.name)

    @patch('siphon.Client.post')
    def test_remove_from_queue(self, response):
        response.return_value = {
            'item': {
                'val': 'bazz'
            }
        }, 201
        queue = Queue(self.Queues, 'foo')
        item = queue.dequeue()
        response.assert_called_with('http://localhost:8000/api/Queues/foo/Dequeue', data={})
        self.assertEqual({
            'val': 'bazz'
        }, item)

        self.assertIsNotNone(queue)  # make sure we still have reference to the instance

    @patch('siphon.Client.delete')
    def test_enqueue(self, response):
        response.return_value = {
            'status': 'enqueued'
        }, 204

        deleted = self.Queues.delete_instance('foo')
        self.assertTrue(deleted)
