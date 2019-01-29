class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        def maxSub(l):
            dp = max_ = l[0]
            for i in range(1, len(l)):
                dp = max(dp + l[i], l[i])
                max_ = max(max_, dp)
            return max_

        if max(A) < 0:
            return max(A)

        r1 = maxSub(A)
        r2 = sum(A) + maxSub([-n for n in A])
        return max(r1, r2)


s = Solution()
print(s.maxSubarraySumCircular([-2,-3,-1]))
