class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []


    def push(self, x: int) -> None:
        self.stack1.append(x)
        if len(self.stack2) == 0:
            self.stack2.append(x)
        else:
            top = self.getMin()
            if top > x:
                self.stack2.append(x)
            else:
                self.stack2.append(top)

    def pop(self) -> None:
        self.stack1.pop()
        self.stack2.pop()

    def top(self) -> int:
        return self.stack1[-1]


    def getMin(self) -> int:
        return self.stack2[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
