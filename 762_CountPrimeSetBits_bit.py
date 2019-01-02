import math
class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        def bit_count(num):
            count = 0
            while num:
                count += 1
                num = num & (num - 1)
            return count

        def is_permie(num):
            if num <= 1:
                return False
            if num == 2 or num == 3:
                return True
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True
        res = 0
        for i in range(L, R + 1):
            count = bit_count(i)
            if is_permie(count):
                res += 1
        return res

    """
    最优解，整数一共32位，所以可以枚举质数，同时利用bin(num).count('1')计算1的数量，学到了
    """
    def countPrimeSetBits2(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        prime = {2, 3, 5, 7, 11, 13, 17, 19}
        count = 0
        for i in range(L, R+1):
            if bin(i).count('1') in prime:
                count += 1
        return count
s = Solution()
s.countPrimeSetBits(10, 15)