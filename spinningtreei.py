import unittest

class UnionFind:
    def __init__(self, size):
        self.size = size
        self.num_components = size
        self.component_size = [1 for i in range(size)]
        self.ids = [i for i in range(size)]

    def find(self, p):
        root = p
        while root != self.ids[root]:
            root = self.ids[root]

        while p != self.ids[p] and self.ids[p] != root:
            next = self.ids[p]
            self.ids[p] = root
            p = next

        return root

    def unify(self, p, q):
        if self.is_connected(p, q):
            return

        root1 = self.find(p)
        root2 = self.find(q)

        if self.component_size[root1] > self.component_size[root2]:
            self.component_size[root1] += self.component_size[root2]
            self.ids[root2] = root1
        else:
            self.component_size[root2] += self.component_size[root1]
            self.ids[root1] = root2

        self.num_components -= 1

    def get_num_of_component(self):
        return self.num_components

    def get_component_size(self, p):
        return self.component_size[self.find(p)]

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    def get_size(self):
        return self.size

def min_cost_to_connect_all_nodes(n, edges, new_edges):
    if not new_edges:
        return 0

    # adjust all node by -1 because Union Find start from 0 but given input start from 1
    for e in edges:
        e[0] -= 1
        e[1] -= 1

    for e in new_edges:
        e[0] -= 1
        e[1] -= 1

    uf = UnionFind(n)

    # Unify all current vertices
    for e in edges:
        uf.unify(e[0], e[1])

    # If all vertices are connected then just return 0
    if uf.get_num_of_component() == 1:
        return 0

    # Sort new edges to apply Krusal MST algorithms
    new_edges.sort(key=lambda e: e[2])
    res = 0

    for e in new_edges:
        fr, to, cost = e[0], e[1], e[2]

        # Skip if already connected
        if uf.is_connected(fr, to):
            continue

        res += cost
        # Unify 2 unconnected components
        uf.unify(fr, to)

        # all nodes are connected
        if uf.get_num_of_component() == 1:
            break

    return res
n = 6
edges = [[1, 4], [4, 5], [2, 3]]
new_edges = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]
result =min_cost_to_connect_all_nodes(n, edges, new_edges)
print (result)
