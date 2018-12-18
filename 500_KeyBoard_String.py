class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # keys = "qwertyuiopasdfghjklzxcvbnm"
        # lines = "11111111112222222223333333"
        # map = dict(zip(keys, lines))
        map = {}
        first = "qwertyuiop"
        second = "asdfghjkl"
        third = "zxcvbnm"
        for f in first:
            map[f] = 1
        for s in second:
            map[s] = 2
        for t in third:
            map[t] = 3
        res = []
        for word in words:
            x = -1
            flag = True
            for w in word.lower():
                if x == -1:
                    x = map[w]
                elif map[w] != x:
                    flag = False
                    break
            if flag:
                res.append(word)
        return res
