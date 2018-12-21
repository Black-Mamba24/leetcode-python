class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        res = 0
        for i, n in enumerate(timeSeries):
            if i + 1 < len(timeSeries):
                res += min(duration, timeSeries[i + 1] -timeSeries[i])
            else:
                res += duration
        return res