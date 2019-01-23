class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - min(nums) * len(nums)
        # smallest = min(nums)
        # res = 0
        # for i, num in enumerate(nums):
        #     res += (num - smallest)
        # return res
        # count = 0
        # nums.sort()
        # while True:
        #     for i in range(len(nums) - 1, 0, -1):
        #         if nums[i] < nums[i - 1]:
        #             nums[i], nums[i - 1] = nums[i - 1], nums[i]
        #         else:
        #             break
        #     smallest = nums[0]
        #     biggest = nums[-1]
        #     if smallest == biggest:
        #         break
        #     else:
        #         # second_biggest = max(list(filter(lambda x: x != biggest, nums)))
        #         second_biggest = nums[-2]
        #         delta = biggest - second_biggest
        #         count += delta
        #         index = nums.index(biggest)
        #         for i in range(len(nums)):
        #             nums[i] += delta
        #         nums[index] -= delta
        # return count

s = Solution()
print(s.minMoves([1,2147483647]))