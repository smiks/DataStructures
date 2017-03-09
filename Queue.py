class Node(object):
    """
        Used for Queue
    """
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Queue(object):
    """
        Single ended queue data structure.
        First In First Out
        Adds element to the left, takes element from the right.
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __repr__(self):
        tmp = ""
        node = self.head
        while node is not None:
            tmp += "{0}, " . format(node.value)
            node = node.next

        tmp = tmp.strip(", ")

        return "Queue({0})" . format(tmp)

    def enqueue(self, value):
        """
            Add from the left (start of the queue).
            O(1)
        """
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node

        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        self.size += 1

    def dequeue(self):
        """
            Take from the right (end of the queue).
            O(1)
        """
        if self.size == 0:
            return None

        if self.size == 1:
            tmp = self.head
            self.head = None
            self.tail = None
            self.size = 0
            return tmp

        tmp = self.tail
        self.tail.prev.next = None
        self.tail = self.tail.prev
        self.size -= 1

        return tmp

    def peek_end(self):
        return self.head

    def peek_front(self):
        return self.tail

    def empty(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

if __name__ == "__main__":

    q = Queue()

    for i in range(1, 6):
        q.enqueue(i)

    print(q)
    print("Size: {0} " . format(len(q)))

    for i in range(5):
        t = q.dequeue()
        print(t.value, end=" ")

    print()
    print(q)
    print("Size: {0} ".format(len(q)))

    for i in range(1, 8, 2):
        q.enqueue(i)

    print(q)
    print("Size: {0} ".format(len(q)))
    _ = q.dequeue()

    print(q)
    print("Size: {0} ".format(len(q)))

    q.empty()
    print("Size: {0} ".format(len(q)))
