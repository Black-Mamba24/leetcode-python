class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        tar = nums[len(nums) // 2]
        res = 0
        for n in nums:
            res += abs(tar - n)
        return res


s = Solution()
print(s.minMoves2([1, 2, 3]))