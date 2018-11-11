class Solution:
    """
    方法一：通用方法， 每个节点都要计算深度
    """

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left = self.deep(root.left)
        right = self.deep(root.right)
        if abs(left - right) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    def deep(self, node):
        if not node:
            return 0
        left = self.deep(node.left)
        right = self.deep(node.right)
        return max(left, right) + 1

    """
    方法二：
    """

    def isBalanced2(self, root):
        def deep(node):
            if not node:
                return 0
            left = deep(node.left)
            right = deep(node.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            else:
                return max(left, right) + 1

        return deep(root) != -1
