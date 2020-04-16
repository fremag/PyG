import os

import cherrypy
from genshi.template import TemplateLoader

from GraphModel import GraphModel


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
        template = self.loader.load('main.html')
        return template.generate(title='Graph Explorer', content='index.html', nodes=self.model.graph.nodes, model=self.model).render('html', doctype='html')

    @cherrypy.expose
    def types(self):
        template = self.loader.load('main.html')
        return template.generate(title='Type stats', content='types.html').render('html', doctype='html')

    @cherrypy.expose
    def type(self, type_name):
        template = self.loader.load('main.html')
        return template.generate(title="Type info", content='type.html', type_name=type_name).render('html', doctype='html')

    @cherrypy.expose
    def node(self, name):
        template = self.loader.load('main.html')
        return template.generate(title="Node info", content='node.html', node=name).render('html', doctype='html')