import heapq


class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacency_list = []


class Edge:
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

    # crucial for heap to be able to compare the edge objects
    def __lt__(self, other_edge):
        return self.weight < other_edge.weight


class PrimsJarnikAlgorithm:
    def __init__(self, unvisited_list):
        # initially store all vertices, then remove one if it is visited
        self.unvisited_list = unvisited_list
        self.mst = []
        self.total_cost = 0
        self.heap = []

    def construct_spanning_tree(self, start_vertex):
        self.unvisited_list.remove(start_vertex)
        current_vertex = start_vertex

        # keep iterating until all the vertices are visited
        # LAZY IMPLEMENTATION
        # PRIMS ALGORITHM IS A GREEDY APPROACH!!
        while self.unvisited_list:
            # consider all the edges of the current vertex
            for edge in current_vertex.adjacency_list:
                if edge.target_vertex in self.unvisited_list:
                    heapq.heappush(self.heap, edge)

            # heapq implement min-heap, and sorting is done by __lt__ method
            min_edge = heapq.heappop(self.heap)

            if min_edge.target_vertex in self.unvisited_list:
                self.mst.append(min_edge)
                print(f"Edge added to spanning tree: {min_edge.start_vertex.value}"
                      f" - {min_edge.target_vertex.value}")
                self.total_cost += min_edge.weight
                current_vertex = min_edge.target_vertex
                self.unvisited_list.remove(current_vertex)

    def get_mst(self):
        return self.mst

    def get_total_cost(self):
        return self.total_cost


if __name__ == '__main__':
    vertexA = Vertex("A")
    vertexB = Vertex("B")
    vertexC = Vertex("C")
    vertexD = Vertex("D")
    vertexE = Vertex("E")
    vertexF = Vertex("F")
    vertexG = Vertex("G")

    # dealing with undirected edges
    # undirected edge = directed edge (u,v) + directed edge (v,u)
    edgeAB = Edge(2, vertexA, vertexB)
    edgeBA = Edge(2, vertexB, vertexA)
    edgeAE = Edge(5, vertexA, vertexE)
    edgeEA = Edge(5, vertexE, vertexA)
    edgeAC = Edge(6, vertexA, vertexC)
    edgeCA = Edge(6, vertexC, vertexA)
    edgeAF = Edge(10, vertexA, vertexF)
    edgeFA = Edge(10, vertexF, vertexA)
    edgeBE = Edge(3, vertexB, vertexE)
    edgeEB = Edge(3, vertexE, vertexB)
    edgeBD = Edge(3, vertexB, vertexD)
    edgeDB = Edge(3, vertexD, vertexB)
    edgeCD = Edge(1, vertexC, vertexD)
    edgeDC = Edge(1, vertexD, vertexC)
    edgeCF = Edge(2, vertexC, vertexF)
    edgeFC = Edge(2, vertexF, vertexC)
    edgeDE = Edge(4, vertexD, vertexE)
    edgeED = Edge(4, vertexE, vertexD)
    edgeDG = Edge(5, vertexD, vertexG)
    edgeGD = Edge(5, vertexG, vertexD)
    edgeFG = Edge(5, vertexF, vertexG)
    edgeGF = Edge(5, vertexG, vertexF)

    unvisited_list = [vertexA, vertexB, vertexC, vertexD, vertexE, vertexF, vertexG]

    vertexA.adjacency_list.append(edgeAB)
    vertexA.adjacency_list.append(edgeAC)
    vertexA.adjacency_list.append(edgeAE)
    vertexA.adjacency_list.append(edgeAF)
    vertexB.adjacency_list.append(edgeBA)
    vertexB.adjacency_list.append(edgeBD)
    vertexB.adjacency_list.append(edgeBE)
    vertexC.adjacency_list.append(edgeCA)
    vertexC.adjacency_list.append(edgeCD)
    vertexC.adjacency_list.append(edgeCF)
    vertexD.adjacency_list.append(edgeDB)
    vertexD.adjacency_list.append(edgeDC)
    vertexD.adjacency_list.append(edgeDE)
    vertexD.adjacency_list.append(edgeDG)
    vertexE.adjacency_list.append(edgeEA)
    vertexE.adjacency_list.append(edgeEB)
    vertexE.adjacency_list.append(edgeED)
    vertexF.adjacency_list.append(edgeFA)
    vertexF.adjacency_list.append(edgeFC)
    vertexF.adjacency_list.append(edgeFG)
    vertexG.adjacency_list.append(edgeGD)
    vertexG.adjacency_list.append(edgeGF)

    # run the algorithm
    algorithm = PrimsJarnikAlgorithm(unvisited_list)
    algorithm.construct_spanning_tree(vertexD)
    print(algorithm.get_total_cost())
