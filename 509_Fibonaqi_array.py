class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 1:
            return N
        f0, f1 = 0, 1
        for i in range(2, N + 1):
            f0, f1 = f1, f0 + f1
        return f1