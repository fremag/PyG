import os
import cherrypy
import networkx as nx
import matplotlib.pyplot as plt
from HtmlServer import HtmlServer
from JsonServer import JsonServer

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
# G = G.reverse()
G = nx.DiGraph()
edges = []
for line in open("e:/tmp/data.txt"):
    items = line.strip().split(",")
    node = items[0].strip()
    nb = items[1].strip()
    if nb == "0":
        continue
    type = items[2].strip()
 #   print("%s: %s, %s, %i" % (node, nb, type, len(items[3:])))
    G.add_node(node, type=type)
    for edge in items[3:]:
        if edge != '':
            strip = edge.strip()
            edges.append([node, strip])

for edge in edges:
#    print("'%s' : '%s'" % (edge[0], edge[1]))
    G.add_edge(edge[0], edge[1])


print("**************************************************")
print("* Dominance                                      *")
print("**************************************************")
dom = nx.dominating_set(G)

for n in G:
    imm_dom = nx.immediate_dominators(G, n)
    if len(imm_dom) > 0:
        print("Node: %s : %i" % (n, len(imm_dom) - 1))
        print(sorted([s for s in imm_dom if s != n]))

print("**************************************************")
print("* Ranks                                          *")
print("**************************************************")
#ranks = nx.voterank(G)
#print(ranks)

print("**************************************************")
print("* Histogram                                      *")
print("**************************************************")
histo = nx.degree_histogram(G)
print(histo)


print("**************************************************")
print("* Info                                           *")
print("**************************************************")
info = nx.info(G)
#print(info)
print("**************************************************")
print("* TEST                                           *")
print("**************************************************")
nodes = list(G.nodes(data='type'))
data = []
for n in nodes:
    node = {"name": n[0], "url": ("/node/%s" % n[0]), "type": n[1]}
    data.append(node)

# nx.draw_spectral(G, with_labels=True)
# plt.show()

html_server = HtmlServer()

json_server = JsonServer()
json_server.init(G)

cherrypy.config.update({
    'tools.encode.on': True,
    'tools.decode.on': True,
    'tools.encode.encoding': 'utf-8',
    'tools.trailing_slash.on': True,
    'tools.staticdir.on': True,
    'tools.staticdir.dir': "static",
    'tools.staticdir.root': os.path.abspath(os.path.dirname(__file__)),
})
# exit()
cherrypy.tree.mount(html_server, '/')
cherrypy.tree.mount(json_server, '/json')
cherrypy.engine.start()
cherrypy.engine.block()

