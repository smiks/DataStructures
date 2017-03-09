class Node(object):
    """
        Node used for Doubly Linked List
    """
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
        self.position = None


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

    def append(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.head.position = 0

        else:
            node.previous = self.tail
            self.tail.next = node
            node.position = node.previous.position + 1

        self.tail = node
        self.size += 1

    def pop(self):
        node = self.tail
        self.tail = self.tail.previous
        self.tail.next = None
        self.size -= 1
        return node

    def insert(self, value, position):
        """
            Insert is O(n) because it has to update positions
        """
        if position >= self.size:
            raise IndexError("Index out of bounds (insert at [{0}])!" . format(position))

        if position == 0:
            raise IndexError("Can not insert at position 0. Use prepend function instead.")
        new_node = Node(value)

        node = self.head
        while node.position < position:
            node = node.next

        new_node.next = node
        new_node.previous = node.previous
        node.previous.next = new_node
        tmp_pos = new_node.previous.position + 1
        new_node.position = tmp_pos
        node = new_node
        while node is not None:
            node.position = tmp_pos
            node = node.next
            tmp_pos += 1

        self.size += 1


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
    ll.insert(999, 3)
    print(ll)

    for e in ll.traverse():
        print("E: {0} P: {1} " . format(e.value, e.position))
