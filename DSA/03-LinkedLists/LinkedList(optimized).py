class Node:
    def __init__(self, value):
        """Initialize a node with a given value."""
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        """Initialize an empty LinkedList."""
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self):
        """Print the values of all nodes in the linked list."""
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def append(self, value):
        """Append a new node with a given value to the end of the linked list."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        """Remove and return the last node from the linked list. """
        if self.length == 0:
            return None
        if self.length == 1:
            removed_node = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return removed_node

        temp = self.head
        while temp.next != self.tail:
            temp = temp.next
        removed_node = self.tail
        self.tail = temp
        self.tail.next = None
        self.length -= 1
        return removed_node


