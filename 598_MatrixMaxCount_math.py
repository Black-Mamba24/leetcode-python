class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        l, r = m, n
        for op in ops:
            l = min(l, op[0])
            r = min(r, op(1))
        return l * r
