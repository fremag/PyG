import cherrypy
import os
from genshi.template import TemplateLoader


class GraphServer(object):
    def __init__(self):
        self.graph = None

        self.loader = TemplateLoader(
            os.path.join(os.path.dirname(__file__), 'templates'),
            auto_reload=True
    )

    @cherrypy.expose
    def index(self):
        template = self.loader.load('index.html')
        return template.generate(title='Graph Explorer').render('html', doctype='html' )

    def init(self, graph):
        self.graph = graph
        pass
