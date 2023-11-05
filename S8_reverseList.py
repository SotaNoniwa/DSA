# Reverse a linked list in-place exercise
# Construct an in-place algorithm (without the need for extra memory) to reverse a linked list!
#
# For example: 1 -> 2 -> 3 -> 4 should be transformed into 4 -> 3 -> 2 -> 1


class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    # O(N) linear running time complexity
    def reverse(self):
    # your algorithm goes here !!!
        current_node = self.head
        previous_node = None
        next_node = None

        while current_node is not None:
            # update next_node
            next_node = current_node.next_node
            # flip the current_node's pointer i.g. 0->1->2 will be 0<-1->2
            current_node.next_node = previous_node
            # update previous_node
            previous_node = current_node
            # update current_node
            current_node = next_node

        # the last node after while loop is now head node
        self.head = previous_node


    def insert(self, data):

        self.size = self.size + 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def get_head(self):
        return self.head

    def traverse_list(self):

        actual_node = self.head

        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.next_node


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.traverse_list()
    print("-"*25)
    linked_list.reverse()
    linked_list.traverse_list()