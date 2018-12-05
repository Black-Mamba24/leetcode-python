from tools.TreeNode import TreeNode


class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        """
        方法一：很慢，重新构建树
        """
        # root = None
        # if t1 and t2:
        #     root = TreeNode(t1.val + t2.val)
        #     root.left = self.mergeTrees(t1.left, t2.left)
        #     root.right = self.mergeTrees(t1.right, t2.right)
        # elif t1:
        #     root = TreeNode(t1.val)
        #     root.left = self.mergeTrees(t1.left, None)
        #     root.right = self.mergeTrees(t1.right, None)
        # elif t2:
        #     root = TreeNode(t2.val)
        #     root.left = self.mergeTrees(None, t2.left)
        #     root.right = self.mergeTrees(None, t2.right)
        # return root

        if t1 and t2:
            t1.val = t1.val + t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
            return t1
        return t1 if t1 else t2