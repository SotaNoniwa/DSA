
class Node:
    def __init__(self, value):
        self.value = value
        self.adjacency_list = []
        self.visited = False


def breadth_first_search(start_node):
    queue = [start_node]

    while queue:
        # remove and return the first item we hae inserted into the list
        current_node = queue.pop(0)
        current_node.visited = True
        print(current_node.value)

        # let's consider the neighbors of the current_node one by one
        for n in current_node.adjacency_list:
            if not n.visited:
                queue.append(n)


if __name__ == '__main__':
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)
    node4.adjacency_list.append(node5)

    breadth_first_search(node1)