class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        flag = 'a'
        for i in  range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    for x in range(len(matrix)):
                        if matrix[x][j]:
                            matrix[x][j] = flag
                    for y in range(len(matrix[i])):
                        if matrix[i][y]:
                            matrix[i][y] = flag

        for i in  range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == flag:
                    matrix[i][j] = 0

s = Solution()
s.setZeroes([[1,1,1],[1,0,1],[1,1,1],[0,1,2]])