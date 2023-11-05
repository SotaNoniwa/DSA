# Finding the middle node in a linked list exercise
# Suppose we have a standard linked list. Construct an in-place (without extra memory)
# algorithm that is able to find the middle node - and return with the middle node!
#
# Note: you should construct an O(N) linear running time algorithm
#
# For example: [1, 2, 3, 4] --> middle node is: 2,   [1, 2, 3, 4, 5] --> middle node is: 3
#
# WE ASSUME THAT WE STORE INTEGERS IN THE LINKED LIST !!!

class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    # O(N) linear running time complexity
    def get_middle_node(self):
    # your implementation goes here !!!
        fast_pointer = self.head
        slow_pointer = self.head

        # when the list has more than two nodes
        while fast_pointer.next_node is not None and fast_pointer.next_node.next_node is not None:
            fast_pointer = fast_pointer.next_node.next_node
            slow_pointer = slow_pointer.next_node

        return slow_pointer



    def insert(self, data):

        self.size = self.size + 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def traverse_list(self):

        actual_node = self.head

        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.next_node


class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None


if __name__ == '__main__':
    linkedList = LinkedList()
    linkedList.insert(1)
    linkedList.insert(2)
    linkedList.insert(3)
    linkedList.traverse_list()
    print("-"*25)
    print(linkedList.get_middle_node().data)
    print("-"*25)
    linkedList.insert(4)
    linkedList.traverse_list()
    print("-"*25)
    print(linkedList.get_middle_node().data)