# inserting item to the beginning of the linked list is O(1)
# while inserting item to the end of the linked list is O(N)
# Linked list overcomes the "hole" problem happens in arrays

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        # head is the first node of the linked list
        self.head = None
        self.num_of_nodes = 0

    # O(1) constant running time
    def insert_start(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        # head is NULL (so the structure is empty)
        if self.head is None:
            self.head = new_node
        # when the linked list is not empty
        else:
            # update references
            new_node.next_node = self.head
            self.head = new_node

    def insert_end(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head

            # find the last node, O(N) linear running time
            while current_node.next_node is not None:
                current_node = current_node.next_node

            # after the loop, current_node is the last node
            current_node.next_node = new_node

    def size_of_list(self):
        return self.num_of_nodes

    def traverse(self):
        current_node = self.head

        while current_node is not None:
            print(current_node)
            current_node = current_node.next_node

    # O(N) linear running time
    def remove(self, data):

        # when the linked list is empty
        if self.head is None:
            return

        # previous_node is needed to update previous_node's reference
        current_node = self.head
        previous_node = None

        # search item we want to remove
        while current_node is not None and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next_node

        # data we want to remove is not in the linked list
        if current_node is None:
            return

        # update the references
        # if previous_node remains None, the head node is the one we want to remove
        if previous_node is None:
            self.head = current_node.next_node
        else:
            # remove an internal node by updating the pointer
            # no need to delete the node because the garbage collector will do that
            previous_node.next_node = current_node.next_node


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_start(10)
    linked_list.insert_start("Adam")
    linked_list.insert_start(7.5)
    linked_list.insert_end(100)
    linked_list.traverse()
    print(25*"-")
    linked_list.remove(1000)
    linked_list.traverse()