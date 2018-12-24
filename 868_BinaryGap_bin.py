class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        str = list(bin(N))[2:]
        res = 0
        last = -1
        for i, s in enumerate(str):
            if s == '1':
                if last == -1:
                    last = i
                else:
                    res = max(res, i - last)
                    last = i
        return res