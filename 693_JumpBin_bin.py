class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = bin(n)[2:]
        last = s[0]
        for i in s[1:]:
            if i != last:
                last = i
            else:
                return False
        return True