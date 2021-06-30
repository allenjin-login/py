

import random
class stack:
    def __init__(self, input_stack):
        self.items = []
        if not input_stack is None:
            self.items = input_stack

    def __str__(self):
        return 'stack:' + str(self.items)

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
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        if isinstance(self,int):
            axc = math_method.change_fraction(self)
            new_num = self.num * axc.den + self.den * axc.num
            new_den = self.den * axc.den

        if isinstance(other,int):
            ax = math_method.change_fraction(other)
            new_num = self.num * ax.den + self.den * ax.num
            new_den = self.den * ax.den
        else:
            new_num = self.num * other.den + self.den * other.num
            new_den = self.den * other.den
        return fraction(new_num, new_den)

    def __sub__(self, other):
        global new_den, new_num
        if isinstance(other,int):
            num_fraction = math_method.change_fraction(other)
            a = math_method.general_division(self, num_fraction)
            new_den = a[0].den
            new_num = a[0].num - a[1].num
        else:
            if self.den == other.den:
                new_den = self.den
                new_num = self.num - other.num
            if self.den != other.den:
                a = math_method.general_division(self, other)
                new_den = a[0].den
                new_num = a[0].num - a[1].num
        return fraction(new_num, new_den)


class math_method:

    def hcf(x, y):
        """该函数返回两个数的最大公约数"""
        # 获取最小值
        global hcf
        if x > y:
            smaller = y
        else:
            smaller = x
        for i in range(1, smaller + 1):
            if (x % i == 0) and (y % i == 0):
                hcf = i
        return hcf

    def gcd(m, n):
        while m % n != 0:
            old_m = m
            old_n = n

            m = old_m
            n = old_m % old_n
        return n

    def gongbei(a, b, int_t=None):
        def gongyue(a, b):
            """
            欧几里得算法----辗转相除法
            :param a: 第一个数
            :param b: 第二个数
            :return: 最大公约数
            """
            # 如果最终余数为0 公约数就计算出来了
            while b != 0:
                temp = a % b
                a = b
                b = temp
            return a

        if int_t is None:
            return a * b / gongyue(a, b)

        if int_t is True:
            return int(a * b / gongyue(a, b))

    def general_division(a, b):
        l = []
        new = math_method.gongbei(a.den, b.den, True)
        new_a_den = a.den * (new / a.den)
        new_a_num = a.num * (new / a.den)
        new_b_den = b.den * (new / b.den)
        new_b_num = b.num * (new / b.den)
        l.append(fraction(int(new_a_num), int(new_a_den)))
        l.append(fraction(int(new_b_num), int(new_b_den)))
        return l

    def change_fraction(input_int):
        return fraction(input_int, 1)


class sort_method:
    def __init__(self,input_list):
        self.list = input_list

    def bubble_sort_flag(list):
        length = len(list)
        for index in range(length):
            # 标志位
            flag = True
            for j in range(1, length - index):
                if list[j - 1] > list[j]:
                    list[j - 1], list[j] = list[j], list[j - 1]
                    flag = False
            if flag:
                # 没有发生交换，直接返回list
                return list
        return list

    def insert_sort(list):
        n = len(list)
        for i in range(1, n):
            # 后一个元素和前一个元素比较
            # 如果比前一个小
            if list[i] < list[i - 1]:
                # 将这个数取出
                temp = list[i]
                # 保存下标
                index = i
                # 从后往前依次比较每个元素
                for j in range(i - 1, -1, -1):
                    # 和比取出元素大的元素交换
                    if list[j] > temp:
                        list[j + 1] = list[j]
                        index = j
                    else:
                        break
                # 插入元素
                list[index] = temp
        return list

    def shell_sort(list):
        n = len(list)
        # 初始步长
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                # 每个步长进行插入排序
                temp = list[i]
                j = i
                # 插入排序
                while j >= gap and list[j - gap] > temp:
                    list[j] = list[j - gap]
                    j -= gap
                list[j] = temp
            # 得到新的步长
            gap = gap // 2
        return list

    def selection_sort(list):
        n = len(list)
        for i in range(0, n):
            min = i
            for j in range(i + 1, n):
                if list[j] < list[min]:
                    min = j
                    list[min], list[i] = list[i], list[min]
        return list

    def merge_sort(list):
        # 认为长度不大于1的数列是有序的
        if len(list) <= 1:
            return list
        # 二分列表
        middle = len(list) // 2
        left = sort_method.merge_sort(list[:middle])
        right = sort_method.merge_sort(list[middle:])
        # 最后一次合并
        return sort_method.merge(left, right)

    def merge(left, right, reslut=None):
        l, r = 0, 0
        result = []
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
            reslut += left[l:]
            result += right[r:]
        return result

    def listrandom(self):
        list = self.list
        for i in range(0, 100000):
            list.append(random  .randint(0, 10000))


class Node:
    def __init__(self,v):
        self.balance = 0
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







