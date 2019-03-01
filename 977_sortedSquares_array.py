class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = [x * x for x in A]
        res.sort()
        return res

s = Solution()
print(s.sortedSquares([-7,-3,2,3,11]))