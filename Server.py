import json
import cherrypy
import os
import networkx as nx
from genshi.template import TemplateLoader


class GraphModel(object):
    def __init__(self, graph):
        self.graph = graph

    def suc(self, name):
        return self.graph.successors(name)

    def dom(self, name):
        dom = nx.immediate_dominators(self.graph, name)
        return [n[0] for n in dom]


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


class HtmlServer(object):
    def __init__(self):
        self.model = None

        self.loader = TemplateLoader(
            os.path.join(os.path.dirname(__file__), 'templates'),
            auto_reload=True
        )

    def init(self, graph):
        self.model = GraphModel(graph)
        pass

    @cherrypy.expose
    def index(self):
        template = self.loader.load('index.html')
        return template.generate(title='Graph Explorer', nodes=self.model.graph.nodes).render('html', doctype='html')

    @cherrypy.expose
    def node(self, name):
        template = self.loader.load('node.html')
        return template.generate(title="Node info", node=name).render('html', doctype='html')
