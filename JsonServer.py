import cherrypy

from GraphModel import GraphModel


class JsonServer(object):
    def __init__(self):
        self.model = None

    def init(self, graph):
        self.model = GraphModel(graph)
        pass

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def dom(self, name):
        return self.model.dom(name)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def suc(self, name):
        result = self.model.suc(name)
        l = []
        for n in result:
            l.append(n)
        return l

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def nodes(self):
        data = [{"name": n, "url": ("/node/%s" % n)} for n in self.model.graph.nodes]
        return data
