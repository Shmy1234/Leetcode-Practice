class MinStack:
    l: list[int]
    m: int

    def __init__(self):
        self.l = []

    def push(self, value: int) -> None:
        if self.l == []:
            self.m = value
        self.l.append(value)
        if self.l[-1] < self.m:
            self.m = value

    def pop(self) -> None:
        if self.m == self.l.pop():
            if self.l != []:
                self.m = min(self.l)

    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        return self.m
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()