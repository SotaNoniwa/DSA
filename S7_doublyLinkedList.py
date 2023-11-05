
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return str(self.data)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # insert items at the end of the linked list
    def insert(self, data):
        new_node = Node(data)

        # when the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # update pointer of new_node
            new_node.previous = self.tail
            # update pointer of tail node (old one)
            self.tail.next = new_node
            # new_node will be the tail now
            self.tail = new_node

    def traverse_forward(self):
        current_node = self.head

        while current_node is not None:
            print(current_node)
            current_node = current_node.next

    def traverse_backward(self):
        current_node = self.tail

        while current_node is not None:
            print(current_node)
            current_node = current_node.previous


if __name__ == '__main__':
    linkedList = DoublyLinkedList()
    linkedList.insert(1)
    linkedList.insert(2)
    linkedList.insert(3)
    linkedList.traverse_forward()
    print("-"*25)
    linkedList.traverse_backward()