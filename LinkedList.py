class Node(object):
    """
        Node used for Doubly Linked List
    """
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LinkedList(object):
    """
        Doubly Linked List
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        node = self.head
        tmp = ""
        while node is not None:
            tmp += "{0}, " . format(node.value)
            node = node.next

        tmp = tmp.strip(", ")
        s = "LinkedList({0})" . format(tmp)

        return s

    def __len__(self):
        return self.size

    def append(self, value):
        """
            Append is O(1)
        """
        node = Node(value)

        if self.head is None:
            self.head = node

        else:
            node.previous = self.tail
            self.tail.next = node

        self.tail = node
        self.size += 1

    def pop(self):
        """
            Pop is O(1)
        """
        node = self.tail
        self.tail = self.tail.previous
        self.tail.next = None
        self.size -= 1
        return node

    def prepend(self, value):
        """
            Prepend is O(1)
        """
        new_node = Node(value)
        self.head.previous = new_node
        new_node.previous = None
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert(self, value, position):
        """
            Insert is O(n)
        """
        if position >= self.size:
            raise IndexError("Index out of bounds (insert at [{0}])!" . format(position))

        if position == 0:
            raise IndexError("Trying to insert at position 0. Use prepend function instead.")

        new_node = Node(value)
        node = self.head
        start_pos = 0
        while start_pos < position:
            node = node.next
            start_pos += 1

        new_node.next = node
        new_node.previous = node.previous
        node.previous.next = new_node

        self.size += 1

    def remove(self, node):

        if self.size == 0:
            raise IndexError("Trying to remove element from empty list.")

        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
            return

        # check if head
        if node.previous is None:
            self.head = node.next
            node.next.previous = None
            node.next = None
            self.size -= 1
            return

        # check if tail
        if node.next is None:
            node.previous.next = None
            node.previous = None
            self.size -= 1
            return

        # in between
        node.next.previous = node.previous
        node.previous.next = node.next
        node.previous = None
        node.next = None
        self.size -= 1

    def search(self, value):
        node = self.head
        if node is None:
            return None

        while node is not None:
            if node.value == value:
                return node

            node = node.next

        return None

    def traverse(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def reverse(self):
        node = self.tail
        while node is not None:
            yield node
            node = node.previous

    def forward(self):
        node = self.head
        while node is not None:
            yield node.value
            node = node.next

    def backward(self):
        node = self.tail
        while node is not None:
            yield node.value
            node = node.previous

if __name__ == "__main__":

    ll = LinkedList()

    print(ll)

    ll.append(5)

    print(ll)

    ll.append(6)
    ll.append(7)
    ll.append(8)

    print(ll)

    print()
    ll.insert(999, 1)
    print(ll)
    ll.prepend(123)
    print(ll)

    for e in ll.traverse():
        print("E: {0}" . format(e.value))

    ll.remove(ll.search(999))
    print(ll)
    ll.remove(ll.search(123))
    print(ll)
    ll.remove(ll.search(8))
    print(ll)
    print("Size: {0} " . format(len(ll)))
