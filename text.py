


class Node:
    def __init__(self,v):
        self.value = v
        if v == None:
            self.value = "null"
        self.left = "null"
        self.right = "null"
    def set_value(self,k):
        self.value = k

    def set_left(self, strxx):
        self.left = strxx

    def set_right(self, stryy):
        self.right = stryy

    def read(self):
        print("v"+str(self.value))
        print(str(self.left))
        print(str(self.right))
    def what(self):
        if not self.left == "null" and not self.right == "null":
            return "all"
        if not self.left == "null":
            return "left"
        if not self.right == "null":
            return "right"
        if self.left == "null" and self.right == "null":
            return "no"

    def node(self):
        if self.left == "null" and self.right == "null":
            print("no")
            return False
        print("t")
        print("left"+str(self.left.value))
        print("right:"+str(self.right.value))

xc = Node("null")

def build(goal,n):
    if goal.value == "null":
        goal.value = n
    if goal.what() == "no":
        if n < goal.value:
            goal.left = Node(n)
        if n > goal.value:
            goal.right = Node(n)
    if goal.what() == "all":
        if n > goal.value:
            build(goal.right,n)
        if n < goal.value:
            build(goal.left,n)
    if goal.what() == "left":
        if n < goal.value:
            goal.left = Node(n)
        if n > goal.value:
            goal.right = Node(n)
    if goal.right == "right":
        if n > goal.value:
            build(goal.right,n)
        if n < goal.value:
            goal.left = Node(n)


if __name__ == '__main__':
    build(xc, 5)
    build(xc, 3)
    build(xc, 7)
    build(xc, 4)

    xc.read()
    xc.node()











