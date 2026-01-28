class MyQueue(object):

    def __init__(self):
        self.Myqueue = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.Myqueue.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        return self.Myqueue.pop(0)
        

    def peek(self):
        """
        :rtype: int
        """
        return self.Myqueue[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.Myqueue) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()