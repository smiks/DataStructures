from collections import defaultdict

class Graph:
    """
        One-way graph
    """
    def __init__(self, directed=True):
        self.edges = defaultdict(list)
        self.distances = {}
        self.num_nodes = 0
        self.directed = directed

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
        if not self.directed:
            self.edges[to_node].append(from_node)
            self.distances[to_node, from_node] = distance

        self.num_nodes = -1

    def get_distance(self, from_node, to_node):
        return self.distances[from_node, to_node]

    def update_distance(self, from_node, to_node, new_distance):
        self.distances[from_node, to_node] = new_distance

    def remove_node(self, node):
        """
            Returns true if node is removed, otherwise False
        """

        node_exists = self.edges.get(node, None)
        if node_exists is None:
            return False

        if not self.directed:
            neighbours = self.edges[node]
            for n in neighbours:
                self.edges[n] = list(filter(lambda x: x != node, self.edges[n]))
        try:
            self.edges.pop(node)
            self.num_nodes = -1
        except KeyError as e:
            return False

        return True

    def purge_graph(self):
        self.edges = defaultdict(list)
        self.distances = {}
        self.num_nodes = 0

    def count_nodes(self):
        if self.num_nodes != -1:
            return self.num_nodes

        if not self.directed:
            return len(self.edges)
        nodes = set()
        for e, neighbours in self.edges.items():
            nodes.add(e)
            for n in neighbours:
                nodes.add(n)

        self.num_nodes = len(nodes)
        return self.num_nodes

    def is_connected_to(self, node_a, node_b):
        """
            Returns true if there is a path from node_a to node_b.
        """
        return node_b in self.edges[node_a]

    def get_path(self, start_node, end_node):
        """
            Returns path from start_node to end_node if it exsists.
            Path is not necessarily the shortest one.

        """

        if start_node == end_node:
            return [start_node]

        if self.edges.get(start_node, None) is None:
            return []

        already_visited = set()
        def _recursive(node, path):
            if node == end_node:
                return path

            if node not in self.edges:
                return None

            path = path + [node]
            for n in self.edges[node]:
                if n in already_visited:
                    continue
                already_visited.add(node)
                new_path = _recursive(n, path)
                if new_path:
                    return new_path
            return None

        path = _recursive(start_node, [])

        return path+[end_node] if len(path) else path




if __name__ == "__main__":

    print("Directed Graph")
    graph = Graph()

    graph.add_edge(0, 1, 3)
    graph.add_edge(0, 3, 1)
    graph.add_edge(0, 2, 1)
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

    path = graph.get_path(0, 4)
    print("Path from 0 to 4: {}" . format(path))

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

    print("\n")

    print("Undirected Graph")
    graph = Graph(directed=False)

    graph.add_edge(0, 1, 3)
    graph.add_edge(0, 3, 1)
    graph.add_edge(0, 2, 1)
    graph.add_edge(3, 4, 2)

    print(graph)

    print("Number of edges: {} ".format(len(graph)))

    num_nodes = graph.count_nodes()
    print("Number of nodes: {} ".format(num_nodes))

    d = graph.get_distance(3, 4)
    print("Distance between nodes 3 and 4: {} ".format(d))

    print("Changing distance between nodes 3 and 4 from 2 to 5")
    graph.update_distance(3, 4, 5)

    d = graph.get_distance(3, 4)
    print("Distance between node 3 and 4: {} ".format(d))

    path = graph.get_path(0, 4)
    print("Path from 0 to 4: {}" . format(path))

    print("Removing node 3")

    graph.remove_node(3)

    print(graph)

    print("Number of edges: {} ".format(len(graph)))

    num_nodes = graph.count_nodes()
    print("Number of nodes: {} ".format(num_nodes))

    print("Purging graph")
    graph.purge_graph()
    num_nodes = graph.count_nodes()
    print(graph)
    print("Number of edges: {} ".format(len(graph)))
    print("Number of nodes: {} ".format(num_nodes))