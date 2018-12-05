class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        j = 0
        for value in pushed:
            stack.append(value)
            while stack and stack[-1] == popped[j]:
                j += 1
                stack.pop()
        return False if stack else True


if __name__ == '__main__':
    s = Solution()
    print(s.validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))
