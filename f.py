class Solution:
    def IsBalanced_Solution(self, pRoot):
        if not pRoot:
            return True
        if self.DeepTree(pRoot) == -1:
            return False
        else:
            return True
    def DeepTree(self, pRoot):
        if not pRoot:
            return 0
        left = self.DeepTree(pRoot.left)
        right = self.DeepTree(pRoot.right)
        if left == -1 or right == -1 or abs(left-right) > 1:
            return -1
        return 1 + max(left, right)