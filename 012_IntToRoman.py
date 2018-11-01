class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        di = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        res = ""
        k = 1
        while num != 0:
            last = num % 10
            num_ = last * k
            if num_ in di:
                res = di[num_] + res
            else:
                if last < 5:
                    i = 0
                    while i < last:
                        res = di[k] + res
                        i = i + 1
                else:
                    tmp = num_
                    while tmp != 5 * k:
                        res = di[k] + res
                        tmp -= k
                    res = di[tmp] + res
            num = int(num / 10)
            k = k * 10
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(188))
