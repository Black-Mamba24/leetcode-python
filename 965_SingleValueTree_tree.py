class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            if root.left and root.right:
                return root.val == root.left.val and self.isUnivalTree(
                    root.left) and root.val == root.right.val and self.isUnivalTree(root.right)
            elif root.left:
                return root.val == root.left.val and self.isUnivalTree(root.left)
            elif root.right:
                return root.val == root.right.val and self.isUnivalTree(root.right)
        return True