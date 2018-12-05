from tools.TreeNode import TreeNode

count = 0
res = None


class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.kth(root, k)
        return res

    def kth(self, node, k):
        if node:
            if node.left:
                self.kth(node.left, k)
            global count
            count += 1
            if count == k:
                global res
                res = node.val
                return
            if node.right:
                self.kth(node.right, k)

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    print(s.kthSmallest(root, 3))