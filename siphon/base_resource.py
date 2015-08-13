import siphon 
from siphon.utils import convert


class InstanceResource(object):
    def __init__(self, base_uri, id):
        self.id = id 
        self.uri = '{base_uri}/{id}'.format(base_uri=base_uri, id=id)
        self.data = dict()

    def fetch(self):
        response = self.request()
        self._loaded = True
        return self._update_instance(response)

    def _load_data(self, response):
        pass


class ListResource(object):
    name = None
    response_key = None
    instance = InstanceResource

    def __init__(self, client, **kwargs):
        self.client = client
        if not self.name:
            self.name = self.__class__.__name__

        if not self.response_key:
            self.response_key = convert(self.name)

        self.uri = '{name}'

    def get_instance(self, id):
        instance = self.instance(self.uri, id)
        return instance
   
   def create(self, **kwargs):
       instance = self.client.request('post', self.uri, data=kwargs)
       return instance

