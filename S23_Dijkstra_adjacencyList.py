import heapq


class Edge:
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex


class Node:
    def __init__(self, value):
        self.value = value
        self.visited = False
        # the node directs to this vertex (previous node) in the shortest path
        self.predecessor = None
        # this is how we store the children
        self.adjacency_list = []
        # this is the sum of edge weight in the shortest path from source vertex
        self.min_distance = float("inf")

    # this is how Python compare objects
    # after inserting these objects into the heap, heap can compare the given objects
    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance


class DijkstraAlgorithm:
    def __init__(self):
        # this is the list (array), but we'll transform this to heap with heapq
        # this is binary heap and not Fibonacci heap
        self.heap = []

    def calculate(self, start_vertex):
        # initialize the vertices
        start_vertex.min_distance = 0
        heapq.heappush(self.heap, start_vertex)

        # have to iterate until the heap becomes empty
        while self.heap:
            # we pop the vertex with the lowest min_distance parameter
            # heapq implements min heap, so it pops the minimum value in self.heap
            current_vertex = heapq.heappop(self.heap)

            # if the vertex is visited, that is, if heap stores the same vertex but with
            # different values, we keep popping it
            if current_vertex.visited:
                continue

            # we have to consider the neighbors
            for edge in current_vertex.adjacency_list:
                u = edge.start_vertex
                v = edge.target_vertex
                new_distance = u.min_distance + edge.weight

                # there is a shorter path to the v vertex
                if new_distance < v.min_distance:
                    # previous vertex in the shortest path
                    v.predecessor = u
                    # update min_distance as we found shorter path
                    v.min_distance = new_distance
                    # update the heap
                    heapq.heappush(self.heap, v)

            current_vertex.visited = True

    # class method vs static method
    # class method takes class as the first parameter (self),
    # static method doesn't need to do it, but can't access class state
    @staticmethod
    def get_shortest_path(vertex):
        print(f"Shortest path to vertex is: {str(vertex.min_distance)}")

        current_vertex = vertex

        while current_vertex:
            print(f"{current_vertex.value} ")
            current_vertex = current_vertex.predecessor


if __name__ == '__main__':
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")
    node8 = Node("H")

    edge1 = Edge(5, node1, node2)
    edge2 = Edge(8, node1, node8)
    edge3 = Edge(9, node1, node5)
    edge4 = Edge(15, node2, node4)
    edge5 = Edge(12, node2, node3)
    edge6 = Edge(4, node2, node8)
    edge7 = Edge(7, node8, node3)
    edge8 = Edge(6, node8, node6)
    edge9 = Edge(5, node5, node8)
    edge10 = Edge(4, node5, node6)
    edge11 = Edge(20, node5, node7)
    edge12 = Edge(1, node6, node3)
    edge13 = Edge(13, node6, node7)
    edge14 = Edge(3, node3, node4)
    edge15 = Edge(11, node3, node7)
    edge16 = Edge(9, node4, node7)

    node1.adjacency_list.append(edge1)
    node1.adjacency_list.append(edge2)
    node1.adjacency_list.append(edge3)
    node2.adjacency_list.append(edge4)
    node2.adjacency_list.append(edge5)
    node2.adjacency_list.append(edge6)
    node8.adjacency_list.append(edge7)
    node8.adjacency_list.append(edge8)
    node5.adjacency_list.append(edge9)
    node5.adjacency_list.append(edge10)
    node5.adjacency_list.append(edge11)
    node6.adjacency_list.append(edge12)
    node6.adjacency_list.append(edge13)
    node3.adjacency_list.append(edge14)
    node3.adjacency_list.append(edge15)
    node4.adjacency_list.append(edge16)

    algorithm = DijkstraAlgorithm()
    algorithm.calculate(node1)
    algorithm.get_shortest_path(node7)