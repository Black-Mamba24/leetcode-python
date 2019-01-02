class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if not matrix:
            return True
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        return True

    def isToeplitzMatrix2(self, matrix):
        """
        进阶，如果矩阵很大，只保存上一行元素。数据量很大的解决原则是只加载当前需要的数据
        :param matrix:
        :return:
        """
        if not matrix:
            return True
        tmp = matrix[0]
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != tmp[j - 1]:
                    return False
            tmp = matrix[i]
        return True
s = Solution()
print(s.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,4]]))