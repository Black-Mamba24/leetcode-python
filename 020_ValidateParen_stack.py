coding=utf-8

class Solution:
    def isValid(self, s):
        """
        最优解，增加一个map，减少代码长度
        :type s: str
        :rtype: bool
        """
        m = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if c in m:
                if not stack or stack.pop() != m[c]:
                    return False
            else:
                stack.append(c)
        return not stack
