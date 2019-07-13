from collections import defaultdict

class Graph:
    """
        One-way graph
    """
    def __init__(self):
        self.edges = defaultdict(list)
        self.distances = {}
        self.num_nodes = 0

    def __len__(self):
        return len(self.edges)

    def __repr__(self):
        ret = ["Graph info: "]
        for e, n in self.edges.items():
            ret.append(f"\tNode: {e} Neighbours: {n}")

        if len(ret) == 1:
            return "Graph info: Empty graph"
        return '\n'.join(ret)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[from_node, to_node] = distance
        self.num_nodes = -1

    def get_distance(self, from_node, to_node):
        return self.distances[from_node, to_node]

    def update_distance(self, from_node, to_node, new_distance):
        self.distances[from_node, to_node] = new_distance

    def remove_node(self, node):
        try:
            self.edges.pop(node)
            self.num_nodes = -1
        except Exception as e:
            print("Node {} not found!" . format(node))

    def purge_graph(self):
        self.edges = defaultdict(list)
        self.distances = {}
        self.num_nodes = 0

    def count_nodes(self):
        if self.num_nodes != -1:
            return self.num_nodes

        nodes = set()
        for e, neighbours in self.edges.items():
            nodes.add(e)
            for n in neighbours:
                nodes.add(n)

        self.num_nodes = len(nodes)
        return self.num_nodes


if __name__ == "__main__":
    graph = Graph()

    graph.add_edge(0, 1, 3)
    graph.add_edge(0, 3, 1)
    graph.add_edge(3, 4, 2)

    print(graph)

    print("Number of edges: {} " . format(len(graph)))

    num_nodes = graph.count_nodes()
    print("Number of nodes: {} " . format(num_nodes))

    d = graph.get_distance(3, 4)
    print("Distance between nodes 3 and 4: {} " . format(d))

    print("Changing distance between nodes 3 and 4 from 2 to 5")
    graph.update_distance(3, 4, 5)

    d = graph.get_distance(3, 4)
    print("Distance between node 3 and 4: {} " . format(d))

    print("Removing node 3")

    graph.remove_node(3)

    print(graph)

    print("Number of edges: {} " . format(len(graph)))

    num_nodes = graph.count_nodes()
    print("Number of nodes: {} " . format(num_nodes))

    print("Purging graph")
    graph.purge_graph()
    num_nodes = graph.count_nodes()
    print(graph)
    print("Number of edges: {} ".format(len(graph)))
    print("Number of nodes: {} " . format(num_nodes))
