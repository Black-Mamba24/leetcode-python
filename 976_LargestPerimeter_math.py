class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        for i in range(len(A) - 1, 1, -1):
            if A[i - 1] + A[i - 2] > A[i]:
                return A[i - 1] + A[i - 2] + A[i]
        return 0


s = Solution()
print(s.largestPerimeter([2, 1, 2]))
