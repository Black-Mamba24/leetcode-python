class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right, maxArea = 0, len(height) - 1, 0

        while left < right:
            # 比较次数更少
            if height[left] < height[right]:
                area = (right - left) * height[left]
                maxArea = max(maxArea, area)
                left = left + 1
            else:
                area = (right - left) * height[right]
                maxArea = max(maxArea, area)
                right = right - 1

        return maxArea