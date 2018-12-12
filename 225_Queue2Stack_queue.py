coding=utf-8
class MyStack:
    def __init__(self):
        """
        python的列表本身具有队列和栈的特性，因此用python实现就是为了练习，直接用一个队列也可以实现
        Initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        if self.q1:
            self.q1.append(x)
        else:
            self.q2.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.q1:
            not_empty = self.q1
            empty = self.q2
        else:
            not_empty = self.q2
            empty = self.q1
        while len(not_empty) > 1:
            empty.append(not_empty.pop(0))
        return not_empty.pop(0)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.q1:
            not_empty = self.q1
            empty = self.q2
        else:
            not_empty = self.q2
            empty = self.q1
        res = 0
        while not_empty:
            if len(not_empty) == 1:
                res = not_empty[0]
            empty.append(not_empty.pop(0))
        return res

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.q1) == 0 and len(self.q2) == 0