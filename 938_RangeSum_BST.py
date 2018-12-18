class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if root:
            val = root.val
            if val < R and val > L:
                return val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
            elif val > R:
                return self.rangeSumBST(root.left, L, R)
            elif val < L:
                return self.rangeSumBST(root.right, L, R)
            elif val == R:
                return val + self.rangeSumBST(root.left, L, R)
            elif val == L:
                return val + self.rangeSumBST(root.right, L, R)
        else: return 0