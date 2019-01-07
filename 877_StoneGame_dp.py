class Solution:
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        total = sum(piles)
        ax = 0
        while piles:
            if piles[0] >= piles[-1]:
                ax += piles[0]
                piles.pop(0)
            else:
                ax += piles[-1]
                piles.pop(-1)
            if ax * 2 > total:
                return True
            if piles[0] >= piles[-1]:
                piles.pop(0)
            else:
                piles.pop(-1)
        return ax * 2 > total