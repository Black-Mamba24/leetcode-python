# coding=utf-8
class Solution:
    #方法一：没花头
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        li = []
        for i in range(num + 1):
            li.append(bin(i).count('1'))
        return li

    #方法二：动态规划，偶数末尾为0，所以1的数量等于除以2后1的数量，奇数则等于前一个偶数数量+1
    def countBits2(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(1, num + 1):
            if i % 2 == 1:
                res.append(res[-1] + 1)
            else:
                res.append(res[num / 2])
        return res
    #最优解：如果是奇数，则x & x - 1为前一个偶数，如果是偶数，则x & x - 1将最高位置为0，其余不变，很棒的算法
    # ans = [0]
    # for x in range(1, num + 1):
    #     ans += ans[x & (x - 1)] + 1,
    # return ans