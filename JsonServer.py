import json

import cherrypy

from GraphModel import GraphModel


class JsonServer(object):
    def __init__(self):
        self.model = None

    def init(self, graph):
        self.model = GraphModel(graph)
        pass

    @cherrypy.expose
    def dom(self, name):
        return json.dumps(self.model.dom(name))

    @cherrypy.expose
    def suc(self, name):
        result = self.model.suc(name)
        l = []
        for n in result:
            l.append(n)
        return json.dumps(l)