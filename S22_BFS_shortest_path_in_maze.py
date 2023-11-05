from collections import deque


class MazeSolver:
    def __init__(self, matrix):
        self.matrix = matrix
        # potential moves: Right(1,0), Up(0,-1), Down(0,1), Left(-1,0)
        self.move_x = [1, 0, 0, -1]
        self.move_y = [0, -1, 1, 0]
        self.visited = [[False for _ in range(len(matrix))] for _ in range(len(matrix))]
        self.min_distance = float("inf")

    def is_valid(self, row, col):
        # outside the table horizontally
        if row < 0 or row >= len(self.matrix):
            return False

        # outside the table vertically
        if col < 0 or col >= len(self.matrix):
            return False

        # obstacle (wall)
        if self.matrix[row][col] == 0:
            return False

        # already visited the given cell
        if self.visited[row][col]:
            return False

        return True

    def search(self, current_x, current_y, destination_x, destination_y):
        self.visited[current_x][current_y] = True
        # the queue is implemented with a doubly linked list - O(1)
        queue = deque()
        queue.append((current_x, current_y, 0))

        while queue:
            # take the first item we have inserted
            (current_x, current_y, dist) = queue.popleft()

            # if we have reached the destination - we break out of the while loop
            if current_x == destination_x and current_y == destination_y:
                self.min_distance = dist
                break

            # iterate potential moves
            for move in range(len(self.move_x)):
                next_x = current_x + self.move_x[move]
                next_y = current_y + self.move_y[move]

                # when move is allowed, append it to the queue (BFS)
                if self.is_valid(next_x, next_y):
                    self.visited[next_x][next_y] = True
                    queue.append((next_x, next_y, dist + 1))

    def show_result(self):
        if self.min_distance != float("inf"):
            print(f"The shortest path from the source to destination: {self.min_distance}")
        else:
            print("No feasible solution - the destination cannot be reached!")


if __name__ == '__main__':

    m = [
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1]
    ]

    maze_solver = MazeSolver(m)
    maze_solver.search(0, 0, 4, 4)
    maze_solver.show_result()
