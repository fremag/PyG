import cherrypy
import collections as col

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
            node = {"name": n[0], "url": ("/node/%s" % n[0]), "type": n[1], "type_url": ("/type/%s" % n[1])}
            data.append(node)
        return data

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def types(self):
        nodes = list(self.model.graph.nodes(data='type'))
        stats = col.defaultdict(int)
        for n in nodes:
            node_type = n[1]
            nb = stats[node_type]
            nb += 1
            stats[node_type] = nb

        data = []
        for node_type in stats:
            s = {"type": node_type, "url": ("/type/%s" % node_type), "count": stats[node_type]}
            data.append(s)

        return data

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def type(self, type_name):
        nodes = [n for n in list(self.model.graph.nodes(data='type')) if n[1] == type_name]
        data = []
        for n in nodes:
            node = {"name": n[0], "url": ("/node/%s" % n[0]), "type": n[1], "type_url": ("/type/%s" % n[1])}
            data.append(node)
        return data
