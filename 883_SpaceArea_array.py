class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for l in grid:
            res += max(l)
            res += len(list(filter(lambda x:x != 0, l)))
        for i in range(len(grid[0])):
            res += max([grid[j][i] for j in range(len(grid))])
        return res

s = Solution()

s.projectionArea([[2]])