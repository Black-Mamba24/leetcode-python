import re


class Solution:
    """
    AC but not fast
    """
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        # key: str，value：出现次数
        m = {}
        max_ = 0
        max_len = 0
        for str in strs:
            if not m.__contains__(str):
                m[str] = 1
            else:
                m[str] = m[str] + 1
            max_ = max(max_, m[str])
        if max_ == 1:
            for k, v in m.items():
                max_len = max(max_len, len(k))
            return max_len
        res = -1
        for k1, v1 in m.items():
            flag = True
            if v1 == 1:
                for k2, v2 in m.items():
                    if k1 != k2 and v2 > 1:
                        if len(k1) > len(k2):
                            res = max(res, len(k1))
                            continue
                        if not self.isSubString(k1, k2):
                            res = max(res, len(k1))
                        else:
                            flag = False
                            break
                if not flag:
                    continue
        return res

    def isSubString(self, shorter, longer):
        partten = "[\s\S]*"
        for c in shorter:
            partten = partten + c + "[\s\S]*"
        return re.match(partten, longer) is not None