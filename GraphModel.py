import networkx as nx


class GraphModel(object):
    def __init__(self, graph):
        self.graph = graph

    def suc(self, name):
        x = self.graph.successors(name)
        return x

    def dom(self, name):
        dom = nx.immediate_dominators(self.graph, name)
        return [n[0] for n in dom]


