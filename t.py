class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.process(root)[0]

    def process(self, node):
        if node is None:
            return True, 0
        leftData = self.process(node.left)
        if not leftData[0]:
            return False, 0
        rightData = self.process(node.right)
        if not rightData[0]:
            return False, 0
        if abs(leftData[1] - rightData[1]) > 1:
            return False, 0
        return True, max(leftData[1], rightData[1]) + 1
