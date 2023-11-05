
class Color:
    RED = 1
    BLACK = 2


class Node:
    def __init__(self, data, parent=None, color=Color.RED):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent
        self.color = color


class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            self.settle_violation(self.root)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:
            if node.left_node:
                self.insert_node(data, node.left_node)
            else:
                node.left_node = Node(data, node)
                self.settle_violation(node.left_node)
        else:
            if node.right_node:
                self.insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)
                self.settle_violation(node.right_node)

    def settle_violation(self, node):
        # Recursively check properties up to the root node
        while node != self.root and self.is_red(node) and self.is_red(node.parent):
            parent_node = node.parent
            grand_parent_node = parent_node.parent

            # parent is a left child of it's parent (so the grandparent)
            if parent_node == grand_parent_node.left_node:
                uncle = grand_parent_node.right_node

                # case 1, 4 (uncle is RED): RECOLORING
                if uncle and self.is_red(uncle):
                    print(f"Re-coloring node {grand_parent_node.data} to RED")
                    grand_parent_node.color = Color.RED
                    print(f"Re-coloring node {parent_node.data} to BLACK")
                    parent_node.color = Color.BLACK
                    uncle.color = Color.BLACK
                    # node will be the grand_parent_node so that we recursively check properties
                    node = grand_parent_node
                else:
                    # case 2: uncle node is black and node is a right child
                    if node == parent_node.right_node:
                        self.rotate_left(parent_node)
                        # node will be the parent_node so that we recursively check properties
                        node = parent_node
                        # we also need to update which will be the next parent, since we rotate
                        # ON parent in case 2
                        # parent_node will be grand_parent_node (notice node is updated one line above)
                        parent_node = node.parent

                    # case 3: re-coloring + rotation on the grandparent
                    parent_node.color = Color.BLACK
                    grand_parent_node.color = Color.RED
                    print(f"Re-color {parent_node.data} to BLACK")
                    print(f"Re-color {grand_parent_node.data} to RED")
                    self.rotate_right(grand_parent_node)

            # we do similar for symmetric case
            # parent is a right child of it's parent (so the grandparent)
            else:
                uncle = grand_parent_node.left_node

                if uncle and self.is_red(uncle):
                    # case 1 and case 4
                    print(f"Re-coloring node {grand_parent_node.data} to RED")
                    grand_parent_node.color = Color.RED
                    print(f"Re-coloring node {parent_node.data} to BLACK")
                    parent_node.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node = grand_parent_node
                else:
                    # case 2: uncle node is black and node is a right child
                    if node == parent_node.left_node:
                        self.rotate_right(parent_node)
                        node = parent_node
                        parent_node = node.parent

                    # case 3
                    parent_node.color = Color.BLACK
                    grand_parent_node.color = Color.RED
                    print(f"Re-coloring {parent_node.data} to BLACK")
                    print(f"Re-coloring {grand_parent_node.data} to RED")
                    self.rotate_left(grand_parent_node)

        if self.is_red(self.root):
            print(f"Re-coloring the root to BLACK...")
            self.root.color = Color.BLACK

    def is_red(self, node):
        # NULL is a leaf node, and it must be black
        if node is None:
            return False

        return node.color == Color.RED

    def traverse(self):
        if self.root:
            self.in_order_traversal(self.root)

    def in_order_traversal(self, node):
        if node.left_node:
            self.in_order_traversal(node.left_node)

        print(node.data)

        if node.right_node:
            self.in_order_traversal(node.right_node)

    def rotate_right(self, node):
        print("Rotating to the right on node ", node.data)

        # update reference TO children
        temp_left_node = node.left_node
        t = temp_left_node.right_node

        temp_left_node.right = node
        node.left_node = t

        # update references TO parent
        if t:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_left_node
        temp_left_node.parent = temp_parent

        # update subtree's (in here, subtree means node, temp_left_node, t) parent's
        # reference TO child
        if temp_left_node.parent:
            if temp_left_node == temp_left_node.parent.left_node:
                temp_left_node.parent.left_node = temp_left_node
            if temp_left_node.parent.right_node == temp_left_node:
                temp_left_node.parent.right_node = temp_left_node
        else:
            self.root = temp_left_node

    def rotate_left(self, node):
        print("Rotating to the left on node ", node.data)

        temp_right_node = node.right_node
        t = temp_right_node.left_node

        temp_right_node.left_node = node
        node.right_node = t

        if t:
            t.parent = node

        temp_parent = node.parent
        temp_right_node.parent = temp_parent
        node.parent = temp_right_node

        if temp_right_node.parent:
            if temp_right_node == temp_right_node.parent.left_node:
                temp_right_node.parent.left_node = temp_right_node
            if temp_right_node == temp_right_node.parent.right_node:
                temp_right_node.parent.right_node = temp_right_node
        else:
            self.root = temp_right_node


if __name__ == '__main__':
    tree = RedBlackTree()
    tree.insert(32)
    tree.insert(10)
    tree.insert(55)
    tree.insert(1)
    tree.insert(19)
    tree.insert(79)
    tree.insert(16)
    tree.insert(23)
    tree.insert(12)