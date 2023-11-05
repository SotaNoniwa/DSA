class Node:
    def __init__(self, data, parent):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent
        self.height = 0


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)
        else:
            print(f"Cannot remove node {data} as AVL tree is empty!")

    def insert_node(self, data, node):
        if data < node.data:
            if node.left_node:
                self.insert_node(data, node.left_node)
            else:
                node.left_node = Node(data, node)
        else:
            if node.right_node:
                self.insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)

        self.update_height(node)
        self.handle_violation(node)

    def remove_node(self, data, node):
        if node is None:
            return

        if data < node.data:
            self.remove_node(data, node.left_node)
        elif data > node.data:
            self.remove_node(data, node.right_node)
        else:
            parent = node.parent

            if node.left_node is None and node.right_node is None:
                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = None
                    if parent.right_node == node:
                        parent.right_node = None
                else:
                    self.root = None

                del node

                self.handle_violation(parent)

            elif node.left_node is not None and node.right_node is None:
                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.left_node
                    if parent.right_node == node:
                        parent.right_node = node.left_node
                else:
                    self.root = node.left_node

                node.left_node.parent = parent

                del node

                self.handle_violation(parent)

            elif node.left_node is None and node.right_node is not None:
                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.right_node
                    if parent.right_node == node:
                        parent.right_node = node.right_node
                else:
                    self.root = node.right_node

                node.right_node.parent = parent

                del node

                self.handle_violation(parent)

            else:
                predecessor = self.get_predecessor(node.left_node)

                node.data = predecessor.data
                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.right_node:
            return self.get_predecessor(node.right_node)
        return node

    def handle_violation(self, node):
        while node is not None:
            self.update_height(node)
            self.balance(node)
            node = node.parent

    def update_height(self, node):
        node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1

    def balance(self, node):
        balance = self.calc_balance(node)

        if balance > 1:
            if self.calc_balance(node.left_node) < 0:
                self.rotate_left(node.left_node)
            self.rotate_right(node)

        if balance < -1:
            if self.calc_balance(node.right_node) > 0:
                self.rotate_right(node.right_node)
            self.rotate_left(node)

    def calc_height(self, node):
        if node is None:
            return -1
        return node.height

    def calc_balance(self, node):
        if node is None:
            return 0
        return self.calc_height(node.left_node) - self.calc_height(node.right_node)

    def rotate_right(self, node):
        print(f"Rotating to the right on node {node.data}")

        temp_left_node = node.left_node
        t = temp_left_node.right_node

        temp_left_node.right_node = node
        node.left_node = t

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_left_node
        temp_left_node.parent = temp_parent

        if temp_left_node.parent is not None:
            if temp_left_node.parent.left_node == node:
                temp_left_node.parent.left_node = temp_left_node
            if temp_left_node.parent.right_node == node:
                temp_left_node.parent.right_node = temp_left_node
        else:
            self.root = temp_left_node

        self.update_height(node)
        self.update_height(temp_left_node)

    def rotate_left(self, node):
        print(f"Rotating to the left on node {node.data}")

        temp_right_node = node.right_node
        t = temp_right_node.left_node

        temp_right_node.left_node = node
        node.right_node = t

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_right_node
        temp_right_node.parent = temp_parent

        if temp_right_node.parent is not None:
            if temp_right_node.parent.left_node == node:
                temp_right_node.parent.left_node = temp_right_node
            if temp_right_node.parent.right_node == node:
                temp_right_node.parent.right_node = temp_right_node
        else:
            self.root = temp_right_node

        self.update_height(node)
        self.update_height(temp_right_node)

    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.left_node:
            self.traverse_in_order(node.left_node)

        l = ""
        r = ""
        p = ""

        if node.left_node is not None:
            l = str(node.left_node.data)
        else:
            l = "NULL"

        if node.right_node is not None:
            r = str(node.right_node.data)
        else:
            r = "NULL"

        if node.parent is not None:
            p = str(node.parent.data)
        else:
            p = "NULL"

        print(f"{node.data} left: {l} right: {r} parent: {p} height: {node.height}")

        if node.right_node:
            self.traverse_in_order(node.right_node)


if __name__ == '__main__':
    avl = AVLTree()
    avl.insert(5)
    avl.insert(3)
    avl.insert(4)
    avl.traverse()
