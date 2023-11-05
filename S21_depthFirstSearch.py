
class Node:
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.adjacency_list = []


def depth_first_search(start_node):
    # we need LIFO data structure, namely Stack
    stack = [start_node]

    while stack:
        current_node = stack.pop()
        print(current_node.value)

        for n in current_node.adjacency_list:
            if not n.visited:
                stack.append(n)


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

    depth_first_search(node1)