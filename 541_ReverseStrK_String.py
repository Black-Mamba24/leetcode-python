class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ''
        for i in range(0, len(s), 2 * k):
            res = res + s[i:i + k][::-1] + s[i + k:i + 2 * k]#如果后面剩余不足k只做第一项，字符串截取左右边界可以超过字符串边界
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.reverseStr("abcdefgh", 3))