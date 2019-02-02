class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        hang, lie, block = {}, {}, {}
        for i in range(9):
            hang[i], lie[i], block[i] = set(), set(), set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                c = board[i][j]
                if c != '.':
                    if c in hang[i] or c in lie[j] or c in block[i // 3 * 3 + j // 3]:
                        return False
                    else:
                        hang[i].add(c)
                        lie[j].add(c)
                        block[i // 3 * 3 + j // 3].add(c)
        return True


s = Solution()
s.isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                 [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                 [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
