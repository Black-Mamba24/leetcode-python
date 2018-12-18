class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for i in range(left, right + 1):
            tmp = i
            flag = True
            while tmp != 0:
                x = tmp % 10
                if x == 0:
                    flag = False
                    break
                tmp = int(tmp / 10)
                if i % x != 0:
                    flag = False
                    break
            if flag:
                res.append(i)
        return res

if __name__ == '__main__':
    s = Solution()
    s.selfDividingNumbers(1, 22)