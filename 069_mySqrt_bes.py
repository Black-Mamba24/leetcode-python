class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x
        while l < r:
            mid = (l + r) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                r = mid - 1
            else:
                l = mid + 1
        return l if l ** 2 <= x else l - 1

s = Solution()
for i in range(2, 100):
    print(i, s.mySqrt(i))