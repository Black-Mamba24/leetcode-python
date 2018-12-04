import math

class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return False
        n = int(math.ceil(math.sqrt(num)))
        sum = 1
        for i in range(2, n):
            if num % i == 0:
               sum += i + num / i
        return sum == num

if __name__ == '__main__':
    s = Solution()
    print(s.checkPerfectNumber(1))
