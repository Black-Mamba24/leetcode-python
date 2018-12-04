class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            return self.check(root.left, root.right)

    def check(self, l, r):
        if l and r:
            return l.val == r.val and self.check(l.left, r.right) and self.check(l.right, r.left)
        return not l and not r
