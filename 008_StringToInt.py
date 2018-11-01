class Solution:
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = ""
        s = s.strip()
        if not len(s):
            return 0
        flag = 1
        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            s = s[1:]
            flag = -1
        for i in range(len(s)):
            if s[i] >= '0' and s[i] <= '9':
                num += s[i]
            else:
                break
        if not len(num):
            return 0
        num = flag * int(num)
        num = min(num, 0x7fffffff)
        num = max(num, -0x80000000)
        return num


if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi("-91283472332"))
