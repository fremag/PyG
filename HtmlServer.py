import os

import cherrypy
from genshi.template import TemplateLoader

from GraphModel import GraphModel


class HtmlServer(object):
    def __init__(self):
        self.loader = TemplateLoader(
            os.path.join(os.path.dirname(__file__), 'templates'),
            auto_reload=True
        )

    def render(self, title, content, **kwargs):
        template = self.loader.load('main.html')
        return template.generate(title=title, content=content, table_style="display", **kwargs).render('html', doctype='html')

    @cherrypy.expose
    def index(self):
        return self.render('Nodes', 'index.html')

    @cherrypy.expose
    def types(self):
        return self.render('Types', 'types.html')

    @cherrypy.expose
    def type(self, type_name):
        return self.render("Type : %s" % type_name, 'type.html', type_name=type_name)

    @cherrypy.expose
    def node(self, name):
        return self.render("Node info", 'node.html', name=name)

    @cherrypy.expose
    def dom_set(self):
        return self.render("Dominating set", 'dom_set.html')

    @cherrypy.expose
    def imm_dom(self, name):
        return self.render("Immediate dominators: "+name, 'imm_dom.html', name=name)

    @cherrypy.expose
    def ranks(self):
        return self.render("Ranks", 'ranks.html')
