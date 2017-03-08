class List(object):

    def __init__(self):
        self.l = []
        self.min = None
        self.max = None
        self.size = 0

    def __getitem__(self, item):
        if not 0 <= item < self.size:
            raise IndexError("Index out of bounds [{0}]!" . format(item))
        return self.l[item]

    def __len__(self):
        return self.size

    def __repr__(self):
        return "List(" + ", ".join(str(e) for e in self.l).strip(", ") + ")"

    def _check_max(self, el):
        if self.max is None:
            self.max = el
            return
        self.max = max(self.max, el)

    def _check_min(self, el):
        if self.min is None:
            self.min = el
            return
        self.min = min(self.min, el)

    def _slow_max_min(self):
        self.min = self.l[0]
        self.max = self.l[0]
        for e in self.l:
            self.min = min(self.min, e)
            self.max = max(self.max, e)

    def append(self, el):
        self.l.append(el)
        self._check_min(el)
        self._check_max(el)

        self.size += 1

    def pop(self):
        el = self.l.pop()
        self._slow_max_min()
        self.size -= 1
        return el

    def peek(self):
        return self.l[-1]

    def empty(self):
        self.l = []
        self.min = None
        self.max = None
        self.size = 0


if __name__ == "__main__":

    """ TEST """

    l = List()

    print(l)

    l.append(5)
    l.append(2)
    l.append(7)

    print(l)
    print("Size: {0} ".format(len(l)))
    print("Max: {0} Min: {1} " . format(l.max, l.min))
    l.pop()
    print("Size: {0} ".format(len(l)))
    print("Max: {0} Min: {1} " . format(l.max, l.min))

    print(l)
    l.empty()
    print(l)
    print("Size: {0} ".format(len(l)))
