from collections import deque
from matplotlib import pyplot as plt


class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.bf = 0
        self.info = None


class AvlTree(object):
    def __init__(self, d_hor=4, d_vec=8, radius=1.5, figsize =(11, 9)):
        """
            对所展示二叉树的一些元素参数的设置
            :param d_hor: 节点与节点的水平距离
            :param d_vec: 节点与节点的垂直距离
            :param radius: 节点的半径
            :param radius: 画布大小，用一个元祖表示画布width和high,单位为inch
            """
        self.root = None
        self.d_hor = d_hor
        self.d_vec = d_vec
        self.radius = radius
        self.figsize = figsize

    def get_left_width(self, root):
        """获得根左边宽度，也是根的左子孙节点数"""
        return self.get_width(root.left_child)

    def get_right_width(self, root):
        """获得根右边宽度，也是根的右子孙节点数"""
        return self.get_width(root.right_child)

    def get_width(self, root):
        """获得树的宽度，也是该树的节点数。使用的是中序遍历方式"""
        if root:
            return self.get_width(root.left_child) + 1 + self.get_width(root.right_child)
        else:
            return 0

    def get_height(self, root):
        """获得二叉树的高度, 使用后序遍历"""
        if root:
            return max(self.get_height(root.left_child), self.get_height(root.right_child)) + 1
        else:
            return 0

    def get_w_h(self, root):
        """获得树的宽度和高度"""
        w = self.get_width(root)
        h = self.get_height(root)
        return w, h

    def __draw_a_node(self, x, y, value, ax):
        """画一个节点"""
        c_node = plt.Circle((x, y), radius=self.radius, color="#65DDFF")
        ax.add_patch(c_node)
        plt.text(x, y, value, ha='center', va='center', fontsize=25, )

    def __draw_a_edge(self, x1, y1, x2, y2):
        """画一条边"""
        x = (x1, x2)
        y = (y1, y2)
        plt.plot(x, y, 'g-')

    def __create_win(self, root):
        """创建窗口"""
        # WEIGHT： 树宽，HEIGHT： 树高
        WEIGHT, HEIGHT = self.get_w_h(root)
        # WEIGHT：树宽 + 1
        WEIGHT = (WEIGHT+1)*self.d_hor
        # HEIGHT = 树高+1
        HEIGHT = (HEIGHT+1)*self.d_vec
        # print(WEIGHT, HEIGHT)

        # fig = plt.figure(figsize=(a, b), dpi=dpi)
        # 设置图形的大小，a 为图形的宽， b 为图形的高，单位为英寸
        # dpi 为设置图形每英寸(inch)的点数
        # 1点（英美点）=0.3527毫米=1/72英寸（Office里面的点）。
        # 线条，标记，文本等大多数元素都有以磅(point即点)为单位的大小。因1inch = 72point,则72dp/inch=1dp/point、144dp/inch=2dp/point
        fig = plt.figure(figsize=self.figsize)
        ax = fig.add_subplot(111)  # 表示整个figure分成1行1列，共1个子图，这里子图在第一行第一列

        plt.xlim(0, WEIGHT)  # 设定x座标轴的范围，当前axes上的座标轴。
        plt.ylim(0, HEIGHT)  # 设定y座标轴的范围，当前axes上的座标轴。
        x = (self.get_left_width(root) + 1) * self.d_hor  # x, y 是第一个要绘制的节点坐标，由其左子树宽度决定
        y = HEIGHT - self.d_vec
        return fig, ax, x, y

    def __print_tree_by_preorder(self, root, x, y, ax):
        """通过先序遍历打印二叉树"""

        if not root:
            # 根节点为空返回
            return

        # 画节点
        self.__draw_a_node(x, y, root.value, ax)

        # 画左右分支
        lx = rx = 0
        ly = ry = y - self.d_vec
        if root.left_child:
            lx = x - self.d_hor * (self.get_right_width(root.left_child) + 1)   # x-左子树的右边宽度
            self.__draw_a_edge(x, y, lx, ly)
            # print(root.left_child, (lx, ly))
        if root.right_child:
            rx = x + self.d_hor * (self.get_left_width(root.right_child) + 1)   # x-右子树的左边宽度
            # print(root.right_child, (rx, ry))
            self.__draw_a_edge(x, y, rx, ry)

        # 递归打印
        self.__print_tree_by_preorder(root.left_child, lx, ly, ax)
        self.__print_tree_by_preorder(root.right_child, rx, ry, ax)

    def show_BSTree_1(self):
        """可视化二叉树"""
        _, ax, x, y = self.__create_win(self.root)
        self.__print_tree_by_preorder(self.root, x, y, ax)
        plt.show()


def insert_avl_tree(avl_tree, key):
    """
    平衡二叉树中插入元素k,使之成为一棵新的平衡二叉排序树

    算法思想：
        (1) 查找应插位置，同时记录离插入位置最近的可能失衡结点A(A的平衡因子不等于0)。
        (2) 插入新结点s。
        (3) 确定结点B，并修改A的平衡因子。
        (4) 修改从B到s路径上的平衡因子(原值必为0，否则A将下移)
        (5) 根据A、B的平衡因子，判断是否失衡以及失衡类型，并做相应处理。

    算法分析：
        平衡二叉排序树插入操作的基本过程是查找操作，所以其时间复杂度是O(log₂n)

    :param avl_tree: 创建好的平衡二叉树
    :param key: 所要插入结点的value值
    :return: 插入结点后的平衡二叉排序树
    """
    s = Node(key)
    if not avl_tree.root:  # 判断所给树是否是棵空树
        avl_tree.root = s
        return avl_tree

    node_A = avl_tree.root  # A结点
    node_FA = None  # A结点的双亲结点
    p = avl_tree.root  # 当前结点
    fp = None  # s的插入位置

    # 首先查找s的插入为fp，同时记录距s的插入位置最近且平衡因子不等于0(等于-1或1)的结点A，A为可能失衡结点
    while p:
        if p.bf != 0:  # 判断当前结点是否是失衡结点
            node_A = p
            node_FA = fp
        fp = p
        if key < p.value:
            p = p.left_child
        else:
            p = p.right_child

    # 插入新结点s
    if key < fp.value:
        fp.left_child = s
    else:
        fp.right_child = s

    # 确定结点B，并修改A的平衡因子
    if key < node_A.value:
        node_B = node_A.left_child
        node_A.bf += 1
    else:
        node_B = node_A.right_child
        node_A.bf -= 1

    # 修改B到s路径上个节点的平衡因子(原值均为0)
    p = node_B
    while p is not s:
        if key < p.value:
            p.bf = 1
            p = p.left_child
        else:
            p.bf = -1
            p = p.right_child

    # 判断失衡类型并做相应处理
    if node_A.bf == 2 and node_B.bf == 1:  # LL型
        node_B = node_A.left_child
        node_A.left_child = node_B.right_child
        node_B.right_child = node_A

        node_A.bf = 0
        node_B.bf = 0

        if not node_FA:
            avl_tree.root = node_B
        elif node_A is node_FA.left_child:
            node_FA.left_child = node_B
        else:
            node_FA.right_child = node_B
    elif node_A.bf == 2 and node_B.bf == -1:  # LR型
        node_B = node_A.left_child
        node_C = node_B.right_child
        node_B.right_child = node_C.left_child
        node_A.left_child = node_C.right_child
        node_C.left_child = node_B
        node_C.right_child = node_A

        if s.value < node_C.value:
            node_A.bf = -1
            node_B.bf = 0
            node_C.bf = 0
        elif s.value > node_C.value:
            node_A.bf = 0
            node_B.bf = 1
            node_C.bf = 0
        else:
            node_A.bf = 0
            node_B.bf = 0

        if not node_FA:
            avl_tree.root = node_C
        elif node_A is node_FA.left_child:
            node_FA.left_child = node_C
        else:
            node_FA.right_child = node_C
    elif node_A.bf == -2 and node_B.bf == -1:  # RR型
        node_B = node_A.right_child
        node_A.right_child = node_B.left_child
        node_B.left_child = node_A

        node_A.bf = 0
        node_B.bf = 0

        if not node_FA:
            avl_tree.root = node_B
        elif node_A is node_FA.left_child:
            node_FA.left_child = node_B
        else:
            node_FA.right_child = node_B
    elif node_A.bf == -2 and node_B.bf == 1:  # RL型
        node_B = node_A.right_child
        node_C = node_B.left_child
        node_A.right_child = node_C.left_child
        node_B.left_child = node_C.right_child
        node_C.left_child = node_A
        node_C.right_child = node_B

        if s.value < node_C.value:
            node_A.bf = 0
            node_B.bf = -1
            node_C.bf = 0
        elif s.value > node_C.value:
            node_A.bf = 1
            node_B.bf = 0
            node_C.bf = 0
        else:
            node_A.bf = 0
            node_B.bf = 0

        if not node_FA:
            avl_tree.root = node_C
        elif node_A is node_FA.left_child:
            node_FA.left_child = node_C
        else:
            node_FA.right_child = node_C
    return avl_tree


def create_avl_tree(key_list: deque):
    """
    创建一棵平衡二叉排序树

    :param key_list: 关键字列表
    :return: 创建好的一棵平衡二叉排序树
    """
    bs_tree = AvlTree()
    for key in key_list:
        bs_tree = insert_avl_tree(bs_tree, key)
    return bs_tree
