class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        m = {}
        res = []
        for i, n in enumerate(nums1):
            if n not in m:
                m[n] = []
            m[n].append(i)
        for n in enumerate(nums2):
            if n in m and m[n]:
                m[n].pop()
                res.append(n)
        return res

if __name__ == '__main__':
    s = Solution()
    s.intersect([2,2,2], [2,2,3])