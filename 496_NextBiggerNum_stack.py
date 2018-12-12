class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        方法一：暴力法
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for n1 in nums1:
            flag = False
            success = False
            for n2 in nums2:
                if n1 == n2:
                    flag = True
                if flag and n2 > n1:
                    res.append(n2)
                    success = True
                    break
            if not success:
                res.append(-1)
        return res

    def nextGreaterElement2(self, nums1, nums2):
        """
        方法二：最优解，利用栈寻找后面第一个更大的元素，并用字典保存，妙哉
        :param nums1:
        :param nums2:
        :return:
        """
        stack = []
        dirc = {}
        for n2 in nums2:
            while stack and stack[-1] < n2:
                dirc[stack.pop()] = n2
            stack.append(n2)
        #return [-1 if n1 not in map else map[n1] for n1 in nums1]
        return [dirc.get(n1, -1) for n1 in nums1] #get方法提供defaultValue