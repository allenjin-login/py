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
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        return fraction(new_num, new_den)

    def __sub__(self, other):
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
            while (b != 0):
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
