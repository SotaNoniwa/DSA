
START_VERTEX_INDEX = 0


class TravellingSalesmanProblem:
    def __init__(self, graph):
        # G(V,E), represented by two-dimensional array
        self.graph = graph
        self.num_of_vertices = len(graph)
        self.visited = [False for _ in range(self.num_of_vertices)]
        # start with the first vertex (we can start with any vertex)
        self.visited[START_VERTEX_INDEX] = True
        # collect all the hamiltonian cycle - we have to get the minimum edge cost cycle
        self.hamiltonian_cycles = []
        # track what vertices are included in the cycle
        self.paths = [0 for _ in range(self.num_of_vertices)]

    def is_valid(self, current_vertex_index, other_vertex_index):
        # when the given vertex has already been visited
        if self.visited[current_vertex_index]:
            return False

        # when there is no connection between the vertices
        if self.graph[current_vertex_index][other_vertex_index] == 0:
            return False

        return True

    def tsp(self, vertex_index, counter, cost):
        # we have considered all the vertices in the G(V,E) graph
        # and the last vertex can be connected to the first one (form a cycle)
        if counter == self.num_of_vertices and self.graph[vertex_index][0]:
            # append the vertex where hamiltonian cycle starts to the end of path
            self.paths.append(START_VERTEX_INDEX)
            print("one possible Hamiltonian cycle (path): " + str(self.paths))
            # we store total cost of the hamiltonian cycle
            self.hamiltonian_cycles.append(cost + self.graph[vertex_index][0])
            # eliminate one path as we append start vertex at the end to form cycle
            self.paths.pop()
            return

        # consider all the vertices in the G(V,E) graph
        # (we filter out the non-adjacent vertices)
        for i in range(self.num_of_vertices):
            # check whether we can include the vertex with index i to the path (cycle)
            if self.is_valid(i, vertex_index):
                self.visited[i] = True
                # we save the vertex's index to keep tracking paths we went through
                self.paths[counter] = i

                # we call the method recursively
                self.tsp(i, counter + 1, cost + self.graph[vertex_index][i])

                # BACKTRACK
                self.visited[i] = False


if __name__ == '__main__':

    g = [[0, 1, 0, 2, 0],
         [1, 0, 1, 0, 2],
         [0, 1, 0, 3, 1],
         [2, 0, 3, 0, 1],
         [0, 2, 1, 1, 0]]

    tsp = TravellingSalesmanProblem(g)
    print(f"We start from the vertex with index {START_VERTEX_INDEX}")
    # we start with the vertex (represented by index 0)
    # counter is 1 because this is the first iteration
    # 0 is the cost so far
    tsp.tsp(0, 1, 0)
    print(f"The minimum Hamiltonian cycle's total cost: {min(tsp.hamiltonian_cycles)}")
