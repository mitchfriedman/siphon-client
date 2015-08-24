class InstanceResource(object):
    def __init__(self, list_resource, name):
        self.name = name
        self.list_resource = list_resource
        self.uri = '{base}/{name}'.format(base=list_resource.uri, name=name)
        self.data = dict()

    def load_data(self, response):
        for k, v in response.items():
            self.data[k] = v

    def __getattr__(self, attr):
        if hasattr(self, attr):
            return self.__getattr__(attr)

        attr = self.data.get(attr, None)

        if attr:
            return attr
        else:
            raise AttributeError

    def get_and_remove_attr(self, attr):
        return self.data.pop(attr, None)


class ListResource(object):
    uri_name = None
    response_key = None
    instance = InstanceResource

    def __init__(self, client):
        self.client = client

        self.uri = '{base}'.format(base=self.client.uri)
        if self.uri_name:
            self.uri += '/{uri_name}'.format(uri_name=self.uri_name)
   
    def create_instance(self, name, **kwargs):
        kwargs['name'] = name
        response, status_code = self.client.post(self.uri, data=kwargs)
        return self._build_instance(response)

    def get_instance(self, name):
        uri = self._build_instance_uri(name)
        response, status_code = self.client.get(uri)
        return self._build_instance(response)

    def update_instance(self, name, **kwargs):
        uri, kwargs = self._build_instance_uri(name, **kwargs)

        response, status_code = self.client.post(uri, data=kwargs)
        return self._build_instance(response)

    def delete_instance(self, name):
        uri = self._build_instance_uri(name)
        response, status_code = self.client.delete(uri)
        if status_code == 204:
            return True
        return False
 
    def _build_instance(self, response):
        name = response.pop('name', None)
        instance = self.instance(self, name)
        instance.load_data(response)
        return instance

    def _build_instance_uri(self, name, **kwargs):
        uri = '{uri}/{name}'.format(uri=self.uri, name=name)
        action = kwargs.pop('action', None)
        if action:
            uri += '/{action}'.format(action=action)

        return uri, kwargs
