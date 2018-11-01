class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        o = x
        if x < 0:
            return False
        num = 0
        while x != 0:
            tmp = x % 10
            x = int(x / 10)
            num = num * 10 + tmp
        return num == o

if __name__ == "__main__":
    s = Solution()
    s.isPalindrome(121)