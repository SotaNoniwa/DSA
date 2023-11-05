
class Node:
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.adjacency_list = []


# we use stack memory in OS, instead of explicitly define stack in code
def depth_first_search(node):
    node.visited = True
    print(node.value)

    for n in node.adjacency_list:
        if not n.visited:
            depth_first_search(n)


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