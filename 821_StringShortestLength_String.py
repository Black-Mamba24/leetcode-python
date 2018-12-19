class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        res = []
        for i, s in enumerate(S):
            if s == C:
                res.append(0)
                continue
            len_ = 1
            while len_ < len(S):
                if i - len_ >= 0:
                    if S[i - len_] == C:
                        res.append(len_)
                        break
                if i + len_ < len(S):
                    if S[i + len_] == C:
                        res.append(len_)
                        break
                len_ += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.shortestToChar2("loveleetcode", 'e'))
