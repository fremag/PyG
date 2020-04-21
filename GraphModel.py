import networkx as nx


class GraphModel(object):
    def __init__(self, graph):
        self.graph = graph

    def suc(self, name):
        x = self.graph.successors(name)
        return x

    def dom(self, name):
        dom = nx.immediate_dominators(self.graph, name)
        return [n for n in dom]

    def nodes(self):
        return self.graph.nodes()

    def dominating_set(self):
        dom = nx.dominating_set(self.graph)
        data = {}
        for n in dom:
            imm_dom = self.immediate_dominators(n)
            data[n] = len(imm_dom) - 1
        return data

    def immediate_dominators(self, node):
        return nx.immediate_dominators(self.graph, node)

    def succ(self, node):
        succ = self.graph.successors(node)
        return succ

    def pre(self, node):
        pre = self.graph.predecessors(node)
        return pre

    def info(self, name):
        node = self.graph.nodes[name]
        node_type = node['type']
        return {'name': name, 'type': node_type, "url": ("/node/%s" % name), "type_url": ("/type/%s" % node_type)}
