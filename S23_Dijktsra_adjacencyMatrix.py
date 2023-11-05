import sys


class DijkstraAlgorithm:
    def __init__(self, adjacency_matrix, start_vertex):
        self.adjacency_matrix = adjacency_matrix
        self.start_vertex = start_vertex
        self.num_of_vertices = len(adjacency_matrix)
        self.visited = [False for _ in range(len(adjacency_matrix))]
        # this stores minimum distance so far, and should be updated if we found shorter path
        self.distances = [float("inf") for _ in range(len(adjacency_matrix))]
        self.distances[start_vertex] = 0

    def get_min_vertex(self):
        # find the vertex with the lowest distance
        min_vertex_value = float("inf")
        min_vertex_index = 0

        # linear search in O(V) linear running time
        # this is why to use heap data structure instead - O(logV)
        for index in range(self.num_of_vertices):
            if not self.visited[index] and self.distances[index] < min_vertex_value:
                min_vertex_value = self.distances[index]
                min_vertex_index = index

        return min_vertex_index

    def calculate(self):
        for vertex in range(self.num_of_vertices):
            # search index of vertex with minimum value, this is the row
            current_vertex = self.get_min_vertex()
            print(f"Considering vertex {current_vertex}")
            self.visited[current_vertex] = True

            # it has again O(V) running time - so the overall running time is quadratic
            # these vertices will be columns
            for other_vertex in range(self.num_of_vertices):
                # make sure if there is path between current_vertex and other_vertex
                if self.adjacency_matrix[current_vertex][other_vertex] > 0:
                    # is there a shorter path to other_vertex to current_vertex?
                    if self.distances[current_vertex] + self.adjacency_matrix[current_vertex][other_vertex] \
                            < self.distances[other_vertex]:
                        self.distances[other_vertex] = self.distances[current_vertex] \
                                                       + self.adjacency_matrix[current_vertex][other_vertex]

    def print_distances(self):
        print(self.distances)


if __name__ == '__main__':

    m = [[0, 7, 5, 2, 0, 0],
         [7, 0, 0, 0, 3, 8],
         [5, 0, 0, 10, 4, 0],
         [2, 0, 10, 0, 0, 2],
         [0, 3, 4, 0, 0, 6],
         [0, 8, 0, 2, 6, 0]]

    algorithm = DijkstraAlgorithm(m, 0)
    algorithm.calculate()
    algorithm.print_distances()
