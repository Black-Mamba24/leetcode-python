class Solution:
    def numJewelsInStones(self, J, S):
        """
        方法一：hash表
        :type J: str
        :type S: str
        :rtype: int
        """
        m = {}
        for s in S:
            if s not in m:
                m[s] = 0
            m[s] += 1
        res = 0
        for j in J:
            if j in m:
                res += m[j]
        return res

    def numJewelsInStones2(self, J, S):
        """
        方法二：两重循环，两种实现相同
        :param J:
        :param S:
        :return:
        """

        # res = 0
        # for s in S:
        #     if s in J:
        #         res += 1
        # return res

        res = 0
        for s in S:
            for j in J:
                if s is j:
                    res += 1