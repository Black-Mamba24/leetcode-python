class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = []
        dict = {}
        for i, x in enumerate(S):
            dict[x] = i
        i = 0
        while i < len(S):
            j = dict[S[i]]
            while i < j:
                i += 1
                print(S[i])
                j = max(j, dict[S[i]])
            res.append(j - i +1)
            i = j + 1
        return res


s = Solution()
print(s.partitionLabels("qiejxqfnqceocmy"))
