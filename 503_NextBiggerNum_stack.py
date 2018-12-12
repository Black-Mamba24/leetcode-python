"""
遇到唤醒数组的问，可以使用拼接法，比较慢但简单；也可以使用两次遍历法，这种方法适用的场景有限
"""
class Solution:
    def nextGreaterElements(self, nums):
        """
        方法一：用数组拼接的方法构造一个长度两倍的数组，用020题目的方法。由于数组拼接，方法很慢
        :type nums: List[int]
        :rtype: List[int]
        """
        new_nums = [x for i in range(2) for x in nums]
        s1 = []  # 值
        s2 = []  # 下标
        dirc = {}
        for i, n in enumerate(new_nums):
            while s1 and s1[-1] < n:
                dirc[str(s1.pop()) + '_' + str(s2.pop())] = n
            s1.append(n)
            s2.append(i)
        return [dirc.get(str(n) + "_" + str(i), -1) for i, n in enumerate(nums)]

    def nextGreaterElements2(self, nums):
        """
        方法二：遍历两次法
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        dirc = {}
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                dirc[stack.pop()] = nums[i]
            stack.append(i)
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                dirc[stack.pop()] = nums[i]
            stack.append(i)
        res = [dirc.get(i, -1) for i in range(len(nums))]
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.nextGreaterElements([1, 2, 1]))