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

    def ranks(self):
        ranks = {}
        level = 0
        for node in self.graph.nodes():
            if len(list(self.graph.successors(node))) == 0:
                ranks[node] = 0

        while len(ranks) != self.graph.number_of_nodes():
            level += 1
            self.rank_node_level(level, ranks)

        return ranks

    def rank_node_level(self, level, ranks):
        rank_level = []
        for node in self.graph.nodes():
            if node in ranks:
                continue
            successors = list(self.graph.successors(node))
            n = 0
            for successor in successors:
                if successor in ranks:
                    n += 1
            if n == len(successors):
                rank_level.append(node)

        for node in rank_level:
            ranks[node] = level

    def build_node(self, node_id, name, children):
        return {'id': node_id, 'text': name, 'children': children}

    def build_tree(self, name, node_id):
        children = []
        node_id += 1
        for succ in self.succ(name):
            child, node_id = self.build_tree(succ, node_id)
            children.append(child)

        data = self.build_node(node_id, name, children)
        return data, node_id

