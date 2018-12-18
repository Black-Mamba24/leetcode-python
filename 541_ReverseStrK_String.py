class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ''
        for i in range(0, len(s), 2 * k):
            res = res + s[i:i + k][::-1] + s[i + k:i + 2 * k]
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.reverseStr("abcd", 2))