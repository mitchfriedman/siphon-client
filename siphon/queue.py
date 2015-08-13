from client.base_client import BaseClient
from client.base_resources import ListResource, InstanceResource


class Queue(InstanceResource):
    pass


class Queues(ListResource):
    # client = BaseClient('http://localhost:8000')
    uri_name  = 'create'
    
    def create(self, **kwargs):
        return self.create(**kwargs)

