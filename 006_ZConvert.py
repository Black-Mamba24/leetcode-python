class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) <= numRows:
            return s
        li = []
        for index in range(numRows):
            li.append("")

        cur = 0
        godwon = False
        for index in range(len(s)):
            li[cur] += s[index]
            if cur == 0 or cur == numRows - 1:
                godwon = ~godwon
            if godwon:
                cur += 1
            else:
                cur -= 1

        res = ""
        for item in li:
            res += item
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3))