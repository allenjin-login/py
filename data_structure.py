class stack:
    def __init__(self, input_stack):
        self.items = []
        if not input_stack is None:
            self.items = input_stack

    def is_empty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
