class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sum = 0
        for n in nums[::2]:
            sum += n
        return sum

        #f 最优解
        nums.sort()
        return sum(nums[::2])

if __name__ == '__main__':
    s = Solution()
    s.arrayPairSum([1,3,2,4])