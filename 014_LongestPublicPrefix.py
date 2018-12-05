class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return 0
        res = ""
        min_ = 0x80000000
        for s in strs:
            min_ = min(min_, len(s))

        for i in range(min_):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if c != strs[j][i]:
                    return res
            res += c

        return res

    def longestCommonPrefix2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        import os
        return os.path.commonprefix(strs)