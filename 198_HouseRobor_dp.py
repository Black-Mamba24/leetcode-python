class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums):
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]

    def rob(self, nums):
        """
        最优解
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for n in nums:
            last, now = now, max(last + n, now)
        return max(last, now)
