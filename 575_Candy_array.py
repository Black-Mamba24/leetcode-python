class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        sister = set(candies)
        return min(len(sister), len(candies)/2)