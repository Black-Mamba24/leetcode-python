class Solution:
    def intersection(self, nums1, nums2):
        """
        方法一：暴力法
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums1:
            if i not in res:
                for j in nums2:
                    if i == j:
                        res.append(i)
                        break
        return res

    def intersection2(self, nums1, nums2):
        s1 = set(nums1)
        s2 = set(nums2)
        return list(nums1 & nums2)


if __name__ == '__main__':
    s = Solution()
    print(s.intersection([1, 2, 2, 1], [2, 2]))
