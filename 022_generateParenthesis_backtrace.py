class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def generate(str, left ,right):
            if left == 0 and right == 0:
                res.append(str)
            else:
                if left > 0:
                    generate(str + '(', left - 1, right)
                if right > left:
                    generate(str + ')', left, right - 1)

        generate('', n, n)
        return res


s = Solution()
print(s.generateParenthesis(4))