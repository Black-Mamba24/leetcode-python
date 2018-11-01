class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        flag = False
        if x < 0:
            x = -x
            flag = True
        while x != 0:
            a = x % 10
            x = int(x / 10)
            res = res * 10 + a
        # max = ~(1 << 31)不能这样用，默认是long型，这样会变成 0xffffffff7fffffffL
        max = 0x7fffffff
        min = -0x80000000

        if res > max or res < min:
            return 0

        if flag:
            return -res
        else:
            return res

    def reverse2(self, x):
        reverse_num = int(str(abs(x))[::-1])
        if reverse_num.bit_length() > 31:
            return 0
        else:
            return reverse_num if x > 0 else -reverse_num


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-4213))