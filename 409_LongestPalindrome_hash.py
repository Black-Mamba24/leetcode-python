class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        m = {}
        for c in s:
            m.setdefault(c, 0)
            m[c] += 1
            if m[c] == 2:
                res += 2
                m[c] = 0
        return res + 1 if sum(m.values()) else res

s = Solution()
print(s.longestPalindrome(s = 'abccccdd'))