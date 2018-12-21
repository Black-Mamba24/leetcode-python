class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        line = 1
        left = 0
        a = ord('a')
        for w in S:
            width = widths[ord(w) - a]
            if left + width > 100:
                line += 1
                left = 0
            left += width
        return [line, left]