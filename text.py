ls = [1, 3, 2]
lsw = [3, 3, 3, 3]
x = [ls, lsw]
print(x)
x = list


class Node:
    def __init__(self,):
        self.value = "null"
        self.left = "null"
        self.right = "null"
    def set_value(self,k):
        self.value = "null"

    def set_left(self, strxx):
        self.left = strxx

    def set_right(self, stryy):
        self.right = stryy

    def read(self):
        print(self.value)
        print(self.left)
        print(self.right)
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
        if self.left == "null" or self.right == "null":
            print("no")
            return False
        print("left:"+str(self.left.value))
        print("right:"+str(self.right.value))

xc = Node()
def build(goal,n):
    # 左小右大
    if goal.what() == "no":
        if goal.value == "null":
            goal.set_value(n)
        if goal.what() == "all":
            if n < goal.left.value:
                goal.left.set_left(n)
            if n > goal.left.value:
                goal.left.set_right(n)
            if n < goal.right.value:
                goal.right.set_left(n)
            if n > goal.right.value:
                goal.right.set_right(n)
        if goal.what() == "left":
            if goal.left.value < n:
                goal.set_right(n)
            if goal.left.value > n:
                goal.left.set_left(n)
        if goal.what() == "right":
            if goal.right.value < n:
                goal.set_left(n)
            if goal.right.value > n:
                goal.right.set_left(n)
        if goal.what() == "no":
            if goal.value == "null":
                goal.set_value(n)
            if n < goal.value:
                goal.set_left(n)
            if n > goal.value:
                goal.set_right(n)






build(xc,1)
build(xc,4)
build(xc,3)


xc.read()
xc.node()




