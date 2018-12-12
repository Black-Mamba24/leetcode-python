coding=utf-8
class MyQueue:
    def __init__(self):
        """
        python的列表本身具有队列和栈的特性，因此用python实现就是为了练习，直接用一个队列也可以实现
        Initialize your data structure here.
        """
        self.input = []
        self.output = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.input.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.output:
            return self.output.pop()
        else:
            while self.input:
                self.output.append(self.input.pop())
            return self.output.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.output:
            return self.output[-1]
        else:
            while self.input:
                self.output.append(self.input.pop())
            return self.output[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.input) == 0 and len(self.output) == 0