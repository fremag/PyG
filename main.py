import os
import cherrypy
import networkx as nx
import matplotlib.pyplot as plt
from Server import GraphServer

G = nx.DiGraph()
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')
G.add_node('E')
G.add_node('F')
G.add_node('G')
G.add_node('H')
G.add_node('I')

G.add_edge('A', 'B')
G.add_edge('A', 'C')
G.add_edge('B', 'D')
G.add_edge('B', 'E')
G.add_edge('C', 'E')
G.add_edge('C', 'F')
G.add_edge('E', 'G')
G.add_edge('E', 'H')
G.add_edge('F', 'I')

# G = nx.read_adjlist("e:/tmp/data2.txt", create_using=nx.DiGraph)

dom = nx.dominating_set(G)

for n in G:
    imm_dom = nx.immediate_dominators(G, n)
    if len(imm_dom) > 0:
        print "Node: %s : %i" % (n, len(imm_dom) - 1)
        print sorted([s[0] for s in imm_dom if s[0] != n])

# nx.draw_spectral(G, with_labels=True)
# plt.show()

server = GraphServer()
server.init(G)
cherrypy.config.update({
    'tools.encode.on': True, 'tools.encode.encoding': 'utf-8',
    'tools.decode.on': True,
    'tools.trailing_slash.on': True,
    'tools.staticdir.root': os.path.abspath(os.path.dirname(__file__)),
})

cherrypy.quickstart(server, '/', {
    '/media': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': 'static'
    }
})

