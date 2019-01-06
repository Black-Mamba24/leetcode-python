import numpy

class Solution:
    def threeSum(self, nums):
        """
        两重循环法
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        res = set()
        nums.sort()
        for i, v in enumerate(nums[:-2]):
            if i >= 0 and v == nums[i - 1]:
                continue
            d = {}
            for x in nums[i + 1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, x, -v-x))
        return map(list, res)


    def threeSum(self, nums):
        """
        双指针法
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        res = []
        nums.sort()
        for i, v in enumerate(nums[:-2]):
            if i >= 0 and v == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if v + nums[l] + nums[r] == 0:
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r - 1] == nums[r]:
                        r -= 1
                elif v + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        return res

if __name__ == '__main__':
    pass