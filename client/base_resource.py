import client


class Resource(object):
    name = None
    response_key = None

    def __init__(self, base_uri=None):
        self.base_uri = base_uri if base_uri else client.api_base
        
        if not self.name:
            self.name = self.__class__.__name__

        if not self.response_key:
            self.response_key = self.name.lower()
         
    def build_list_uri(self, id):
        return '{}/{}/{}'.format(self.base_uri, self.name, id)

    def build_instance_uri(self):
        return '{base_uri}/{name}'.format(self.base_uri, self.name)


class InstanceResource(Resource):
    pass


class ListResource(Resource):
    instance = InstanceResource

    def __init__(self, **kwargs):
        super(ListResource, self).__init__(**kwargs)

    def get_instance(self, id):
        uri = self.build_instance_uri()
        
