class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        res = self.subTree(root)
        return root if res else None

    def subTree(self, node):
        if not node:
            return False
        else:
            # True表示保留，False表示剪枝
            left = self.subTree(node.left)
            right = self.subTree(node.right)
            if not left:
                node.left = None
            if not right:
                node.right = None
            return node.val != 0 or left or right
