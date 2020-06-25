import os
import cherrypy
import networkx as nx
from HtmlServer import HtmlServer
from JsonServer import JsonServer

G = nx.DiGraph()
edges = []
for line in open("e:/tmp/data.txt"):
    items = line.strip().split(",")
    node = items[0].strip()
    type = items[1].strip()
    #   print("%s: %s, %s, %i" % (node, nb, type, len(items[3:])))
    G.add_node(node, type=type)
    for edge in items[2:]:
        if edge != '':
            strip = edge.strip()
            edges.append([node, strip])

for edge in edges:
    #    print("'%s' : '%s'" % (edge[0], edge[1]))
    G.add_edge(edge[0], edge[1])

html_server = HtmlServer()

json_server = JsonServer()
json_server.init(G)

root = os.path.abspath(os.path.dirname(__file__))
config = {'/static': {'tools.staticdir.on': True,
                      'tools.staticdir.dir': "static",
                      'tools.staticdir.root': root}
          }

cherrypy.tree.mount(html_server, '/', config)
cherrypy.tree.mount(json_server, '/json')
cherrypy.config.update({
    'tools.encode.on': True,
    'tools.decode.on': True,
    'tools.encode.encoding': 'utf-8',
    'tools.trailing_slash.on': True
})

cherrypy.engine.start()
cherrypy.engine.block()
