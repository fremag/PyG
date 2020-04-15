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
        successors = list(result)
        return successors

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def nodes(self):
        nodes = list(self.model.graph.nodes(data='type'))
        data = []
        for n in nodes:
            node = {"name": n[0], "url": ("/node/%s" % n[0]), "type": n[1]}
            data.append(node)
        return data
