class Solution:

    def isBalanced(self, root):

        def height(root):
            """
            获得以root为根结点的树的最大深度
            :param root:
            :return:
            """
            if root is None:
                return 0
            return max(height(root.left), height(root.right)) + 1

        def is_balanced(root):
            """
            判定是否为平衡二叉树
            :param root:
            :return:
            """
            if root is None:        # 如果是空树
                return True         # 一定是平衡二叉树

            # 满足平衡二叉树的条件：左右子树平衡，左右子树最大深度差值不大于1
            return is_balanced(root.left) and is_balanced(root.right) and \
                   abs(height(root.left)-height(root.right)) <= 1

        return is_balanced(root)
