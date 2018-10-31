class Solution:
    start = 0
    maxLen = 0

    """
    方法一：中心扩展法
    """

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        for i in range(len(s)):
            self.helper(i, i, s)
            self.helper(i, i + 1, s)
        return s[self.start:self.start + self.maxLen]

    def helper(self, i, j, s):
        """
        :param i: 中心扩展左下标
        :param j: 中心扩展右下标
        :param s: 字符串
        """
        while True:
            if i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            else:
                break

            tmp = j - i - 1
            if tmp > self.maxLen:
                self.start = i + 1
                self.maxLen = tmp

    """
    方法二：动态规划法，回文长度可能是奇数或偶数，分情况计算
    """

    def longestPalindrome2(self, s):
        n = len(s)
        maxl = 0
        start = 0
        for i in range(n):
            """
            优先从i - maxl - 1 到 i，判断是否是回文，最少判断连续3个字符，得到一个回文后，下一次计算利用上一次计算的结果，不重复计算长度小于当前maxLen的子串，下面的同理
            """
            if i - maxl - 1 >= 0 and s[i - maxl - 1: i + 1] == s[i - maxl - 1: i + 1][::-1]:
                start = i - maxl - 1
                maxl += 2
                continue
            """
            如果i - maxl - 1 到 i不是回文，再尝试i - maxl 到 i是否是回文，最少判断连续两个字符
            """
            if i - maxl >= 0 and s[i - maxl: i + 1] == s[i - maxl: i + 1][::-1]:
                start = i - maxl
                maxl += 1
        return s[start: start + maxl]


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome2("fejwionabaecsa"))
