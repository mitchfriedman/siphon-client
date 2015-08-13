import siphon 
from siphon.utils import convert


class InstanceResource(object):
    id_key = None

    def __init__(self, list_resource, id):
        self.id = id 
        self.uri = '{base_uri}/{id}'.format(base_uri=list_resource.uri, id=id)
        self.data = dict()

    def load_data(self, response):
        for k, v in response.items():
            self.data[k] = v

    def __getattr__(self, attr):
        if hasattr(self, attr):
            return self.__getattribute__(attr)
        attr = self.data.get(attr, None)
        if attr:
            return attr
        else:
            raise AttributeError

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
   
    def create_instance(self, **kwargs):
        response, status_code = self.client.post(self.uri, data=kwargs)
        return self.build_instance(response)

    def get_instance(self, id):
        uri = self._build_instance_uri(id)
        response, status_code = self.client.get(uri)
        return self._build_instance(response)

    def update_instance(self, id, **kwargs):
        uri = self._build_instance_uri(id)
        response, status_code = self.client.post(uri, data=kwargs)
        return self._build_instance(response)

    def delete_instance(self, id):
        uri = self._build_instance_uri(id)
        response, status_code = self.client.delete(uri)
        if response.status_code == 204:
            return True
        return False
 
    def _build_instance(self, response):
        id = response.pop('id', None)
        instance = self.instance(self, id)
        instance.load_data(response)
        return instance

    def _build_instance_uri(self, id):
        return '{uri}/{id}'.format(uri=self.uri, id=id)

