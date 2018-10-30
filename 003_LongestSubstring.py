class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        方法一：双指针 + set，不重复放入，计算最大，移动end指针；
            如果重复则移动start指针，删除集合中对应的元素，直到删掉重复元素
        """
        set_ = set()
        start = end = 0
        l = list(s)
        res = 0
        while (end < len(s)):
            c = s[end]
            if not c in set_:
                set_.add(c)
                res = max(res, len(set_))
                end = end + 1
            else:
                while s[start] != c:
                    set_.remove(s[start])
                    start = start + 1
                set_.remove(s[start])
                start = start + 1
        return res

    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        方法二：双指针 + map，k：值，v：下标
            不重复放入，计算最大值，移动end指针，由于没有依次删掉重复数据前面的kv，可能有些kv落后于start，所以如果落后视为不包含
            如果重复，start指针置为原下标+1，跳过重复值，并设置新下标
        """
        di = {}
        res = 0
        start = end = 0
        while end < len(s):
            c = s[end]
            if not c in di or di[c] < start:
                di[c] = end
                res = max(res, end - start + 1)
            else:
                start = di[c] + 1
                di[c] = end
            end += 1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring2("pwwkew"))