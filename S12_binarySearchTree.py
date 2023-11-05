
class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent


class BinarySearchTree:
    def __init__(self):
        # we can access the root node exclusively
        self.root = None

    def insert(self, data):
        # when inserting the first node in the tree
        if self.root is None:
            self.root = Node(data)
        # when BST is not empty
        else:
            self.insert_node(data, self.root)

    # "data" is the node what we want to insert
    # "node" is where to insert, namely, it'll be the parent of "data"
    #        node           node
    #        /  \     or    /  \
    #     data                 data
    def insert_node(self, data, node):
        # we go to the left subtree if data is less than node
        if data < node.data:
            # when the left_node exists, we keep going till we reach a leaf node
            if node.left_node:
                self.insert_node(data, node.left_node)
            # when there's no left child, we insert data
            else:
                node.left_node = Node(data, node)
        # we go to the right subtree
        else:
            if node.right_node:
                self.insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)
        else:
            print(f"Removing {data} fail as BST is empty!")

    def remove_node(self, data, node):
        # when data is not in BST, we keep calling method even deeper than leaf node, then it ends up that node is None
        if node is None:
            print(f"Node {data} doesn't exist")
            return

        if data < node.data:
            self.remove_node(data, node.left_node)
        elif data > node.data:
            self.remove_node(data, node.right_node)
        else:
            # we found the node we want to remove (node has the same value as data)
            # there are 3 scenarios

            # initialize parent variable
            parent = node.parent

            # CASE 1: remove a leaf node
            if node.left_node is None and node.right_node is None:
                print(f"Removing a leaf node... {node.data}")

                # we must update parent's references
                # the leaf node is left child of its parent
                if parent is not None and parent.left_node == node:
                    parent.left_node = None

                # the leaf node is right child of its parent
                if parent is not None and parent.right_node == node:
                    parent.right_node = None

                # the leaf node is a root node
                if parent is None:
                    self.root = None

                del node

            # CASE 2: remove a node with single child
            elif node.left_node is None and node.right_node is not None:
                print(f"Removing a node {node.data} with single right child {node.right_node.data}")

                if parent is not None and parent.left_node == node:
                    parent.left_node = node.right_node

                if parent is not None and parent.right_node == node:
                    parent.right_node = node.right_node

                if parent is None:
                    self.root = node.right_node

                # update right child's parent
                node.right_node.parent = parent

                del node

            elif node.right_node is None and node.left_node is not None:
                print(f"Removing a node {node.data} with single left child {node.left_node.data}")

                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.left_node
                    if parent.right_node == node:
                        parent.right_node = node.left_node
                else:
                    self.root = node.left_node

                node.left_node.parent = parent

                del node

            # CASE 3: remove a node with 2 children
            else:
                print(f"Removing a node {node.data} with two children, L: {node.left_node.data}, R: {node.right_node.data}")

                # search predecessor, the largest node in left subtree
                predecessor = self.get_predecessor(node.left_node)

                # swap the node we want to remove and predecessor
                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                # we've already make sure the "node" has the same value as "data"
                # then swapped "node" and "predecessor"
                # now "data" and "predecessor" has the same value
                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.right_node:
            return self.get_predecessor(node.right_node)

        return node

    def get_min(self):
        if self.root:
            return self.get_min_value(self.root)

    def get_min_value(self, node):
        if node.left_node:
            return self.get_min_value(node.left_node)

        return node.data

    def get_max(self):
        if self.root:
            return self.get_max_value(self.root)

    def get_max_value(self, node):
        if node.right_node:
            return self.get_max_value(node.right_node)

        return node.data

    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root)

    # O(N) linear running time
    def traverse_in_order(self, node):
        if node.left_node:
            self.traverse_in_order(node.left_node)

        print(node.data)

        if node.right_node:
            self.traverse_in_order(node.right_node)


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(2)
    bst.insert(7)
    bst.insert(1)
    bst.insert(4)
    bst.insert(6)
    bst.insert(14)

    bst.remove(5)

    bst.traverse()

    print(f"Max value: {bst.get_max()}")
    print(f"Min value: {bst.get_min()}")