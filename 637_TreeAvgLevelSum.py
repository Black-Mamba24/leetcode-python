import queue
from TreeNode import *


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return 0

        q = queue.Queue()
        q.put(root)
        res = []
        while q.qsize():
            size = q.qsize()
            sum = 0
            for i in range(0, size):
                node = q.get()
                sum += node.val
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            if size:
                res.append(sum / size)
        return res


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print( s.averageOfLevels(root))
