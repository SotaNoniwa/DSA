
class Vertex:
    # instance of Vertex is the vertex or node in the G(V,E)
    def __init__(self, value):
        self.value = value
        # and this represents the node in disjoint set
        self.node = None


class Edge:
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

    # Kruskal's algorithm sorts the edges by the weights
    def __lt__(self, other_edge):
        return self.weight < other_edge.weight


class Node:
    # node in the tree representation of the disjoint set
    def __init__(self, rank, node_id, parent=None):
        self.rank = rank
        self.node_id = node_id
        self.parent = parent


class DisjointSet:
    def __init__(self, vertex_list):
        self.vertex_list = vertex_list
        # this stores representatives (root nodes) of each disjoint set
        self.representatives = []
        self.make_sets()

    def make_sets(self):
        for v in self.vertex_list:
            # 2nd param, node_id will be 0, 1, 2...
            node = Node(0, len(self.representatives))
            v.node = node
            self.representatives.append(node)

    # the aim of the find() function is to find the root node which is the representative
    # of that given disjoint set
    @staticmethod
    def find(node):
        current_node = node

        # find the representative (root node)
        while current_node.parent:
            current_node = current_node.parent

        representative = current_node
        # re-initialize current_node
        current_node = node

        # apply path compression
        # make sure that all the nodes are pointing to the representative
        while current_node is not representative:
            temp = current_node.parent
            current_node.parent = representative
            current_node = temp

        return representative.node_id

    def merge(self, node1, node2):
        # find representatives
        index1 = self.find(node1)
        index2 = self.find(node2)

        # if these nodes are in the same disjoint set, we can't merge them
        if index1 == index2:
            return

        # merge by rank parameters
        representative1 = self.representatives[index1]
        representative2 = self.representatives[index2]

        if representative1.rank < representative2.rank:
            representative1.parent = representative2
        elif representative1.rank > representative2.rank:
            representative2.parent = representative1
        else:
            # representative2.parent = representative1 is also valid as their rank are the same
            representative1.parent = representative2
            representative1.rank += 1


class KruskalAlgorithm:
    def __init__(self, vertex_list, edge_list):
        self.vertex_list = vertex_list
        self.edge_list = edge_list

    def construct_mst(self):
        disjoint_set = DisjointSet(self.vertex_list)
        minimum_spanning_tree = []

        # sort the edges based on the weight
        # sort() knows how to compare thanks to  __lt__ method in Edge class
        self.edge_list.sort()

        for edge in self.edge_list:
            u = edge.start_vertex
            v = edge.target_vertex

            # when two vertices are in the different disjoint sets,
            # we add edge in MST and merge two disjoint sets
            if disjoint_set.find(u.node) is not disjoint_set.find(v.node):
                minimum_spanning_tree.append(edge)
                disjoint_set.merge(u.node, v.node)

        print("start vertex - target vertex - edge weight")
        for edge in minimum_spanning_tree:
            print(edge.start_vertex.value, " - ", edge.target_vertex.value, "- ", edge.weight)


if __name__ == '__main__':
    vertex1 = Vertex("A")
    vertex2 = Vertex("B")
    vertex3 = Vertex("C")
    vertex4 = Vertex("D")
    vertex5 = Vertex("E")
    vertex6 = Vertex("F")
    vertex7 = Vertex("G")

    edge1 = Edge(2, vertex1, vertex2)
    edge2 = Edge(6, vertex1, vertex3)
    edge3 = Edge(5, vertex1, vertex5)
    edge4 = Edge(10, vertex1, vertex6)
    edge5 = Edge(3, vertex2, vertex4)
    edge6 = Edge(3, vertex2, vertex5)
    edge7 = Edge(1, vertex3, vertex4)
    edge8 = Edge(2, vertex3, vertex6)
    edge9 = Edge(4, vertex4, vertex5)
    edge10 = Edge(5, vertex4, vertex7)
    edge11 = Edge(5, vertex6, vertex7)

    vertices = []
    vertices.append(vertex1)
    vertices.append(vertex2)
    vertices.append(vertex3)
    vertices.append(vertex4)
    vertices.append(vertex5)
    vertices.append(vertex6)
    vertices.append(vertex7)

    edges = []
    edges.append(edge1)
    edges.append(edge2)
    edges.append(edge3)
    edges.append(edge4)
    edges.append(edge5)
    edges.append(edge6)
    edges.append(edge7)
    edges.append(edge8)
    edges.append(edge9)
    edges.append(edge10)
    edges.append(edge11)

    algorithm = KruskalAlgorithm(vertices, edges)
    algorithm.construct_mst()
