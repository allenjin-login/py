class stack:
    def __init__(self, input_stack):
        self.items = []
        if not input_stack is None:
            self.items = input_stack

    def __str__(self):
        return 'stack:' + self.items

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self, input_stack):
        self.items = []
        if not input_stack is None:
            self.items = input_stack

    def __str__(self):
        return 'Queue' + self.items

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den

        return fraction(new_num,new_den)


