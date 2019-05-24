class RouteConfig():
    def __init__(self, host):
       self.host = host
       self.routes = {}
    def register_route(self, key, value):
        self.routes[key] = '{}{}'.format(self.get_api_url(),value)    
    def get_api_url(self):
        return '{}/api'.format(self.host)
    def get_route(self, key):
        return self.routes[key]