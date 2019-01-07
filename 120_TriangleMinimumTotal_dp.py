class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        sum_ = triangle[-1]
        for i in range(len(triangle) - 2, -1 ,-1):
            for j, value in enumerate(triangle[i]):
                sum_[j] = value + min(sum_[j], sum_[j + 1])
        return sum_[0]