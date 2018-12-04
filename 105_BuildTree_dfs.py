from tools.TreeNode import TreeNode


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        def build(preorder, inorder, p_start, p_end, i_start, i_end):
            if p_start > p_end or i_start > i_end:
                return None
            val = preorder[p_start]
            len_ = inorder.index(val) - i_start
            node = TreeNode(val)
            node.left = build(preorder, inorder, p_start + 1, p_start + len_, i_start, i_start + len_ - 1)
            node.right = build(preorder, inorder, p_start + len_ + 1, p_end, i_start + len_ + 1, i_end)
            return node

        return build(preorder, inorder, 0, len(preorder) - 1, 0, len(inorder) - 1)
