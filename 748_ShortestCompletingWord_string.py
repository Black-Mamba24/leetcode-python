class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        array = [0] * 26
        a = ord('a')
        for x in licensePlate:
            if x.isalpha():
                array[ord(x.lower()) - a] += 1
        min = 0xffffffff
        min_value = 0
        for word in words:
            tmp = array[:]
            flag = True
            for c in word:
                index = ord(c.lower()) - a
                if tmp[index]:
                    tmp[index] -= 1
            if flag and sum(tmp) == 0:
                if len(word) < min:
                    min = len(word)
                    min_value = word
        return min_value if min != 0xffffffff else None

    def shortestCompletingWord(self, licensePlate, words):
        """
        最优解
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        plate = [s.lower() for s in licensePlate if s.isalpha()]
        for word in sorted(words, key=len):
            temp = plate.copy()
            for c in word:
                if c in temp:
                    del temp[temp.index(c)]
            if len(temp) == 0:
                return word


s = Solution()
print(s.shortestCompletingWord("1s3 PSt", ["step", "steps", "stripe", "stepple"]))
