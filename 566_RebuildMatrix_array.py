class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if not nums:
            return nums
        old_r = len(nums)
        old_c = len(nums[0])
        if r * c !=  old_r * old_c:
            return nums
        all = [item for line in nums for item in line]
        line = []
        res = []
        for i, x in enumerate(all):
            line.append(x)
            if (i + 1) % c == 0:
                res.append(line)
                line = []
        return res