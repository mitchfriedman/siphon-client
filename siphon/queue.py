from siphon.base_resource import ListResource, InstanceResource


class Queue(InstanceResource):
    def dequeue(self):
        return self.list_resource.dequeue(self.name, action='Dequeue')


class Queues(ListResource):
    uri_name = 'Queues'

    def create(self, **kwargs):
        return self.create(**kwargs)

    def dequeue(self, instance_name, **kwargs):
        instance_resource = self.update_instance(instance_name, **kwargs)
        item = instance_resource.get_and_remove_attr('item')
        return item
