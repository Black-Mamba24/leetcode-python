class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        if not grid:
            return 0
        chang = len(grid[0])
        kuan = len(grid)
        dic = {}
        for i, l in enumerate(grid):
            for j, value in enumerate(l):
                key = i << 32 | j
                dic[key] = value

        for i, l in enumerate(grid):
            for j, value in enumerate(l):
                key = i << 32 | j
                if dic[key]:
                    # up
                    up, down, left, right = 0,0,0,0
                    if i - 1 < 0:
                        up = 1
                    else:
                        up = 0 if dic[(i - 1) << 32 | j] == 1 else 1

                    if i + 1 > kuan - 1:
                        down = 1
                    else:
                        down = 0 if dic[(i + 1) << 32 | j] == 1 else 1

                    if j - 1 < 0:
                        left = 1
                    else:
                        left = 0 if dic[i << 32 | (j - 1)] == 1 else 1

                    if j + 1 > chang - 1:
                        right = 1
                    else:
                        right = 0 if dic[i << 32 | (j + 1)] == 1 else 1

                    res += (up + down + left + right)
        return res

if __name__ == '__main__':
    s = Solution()
    s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])