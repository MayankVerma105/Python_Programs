class Queue:

    def __init__(self):
        self.values = list()

    def enqueue(self, element):
        self.values.append(element)

    def dequeue(self):
        if not(self.isEmpty()):
            return self.values.pop(0)
        else:
            print('Queue Underflow')
            return None

    def isEmpty(self):
        return len(self.values) == 0

    def front(self):
        if not (self.isEmpty()):
            return self.values[0]
        else:
            print('Queue Empty')
            return None

    def size(self):
        return len(self.values)

    def __str__(self):
        stringRepr = ''
        for i in self.values:
            stringRepr += str(i) + '\t'
        return stringRepr
