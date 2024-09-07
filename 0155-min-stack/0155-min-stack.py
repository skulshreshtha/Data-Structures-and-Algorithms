import numpy as np
class MinStack:

    def __init__(self):
        self._stack = [] # Will store tuples
        
    def push(self, val: int) -> None:
        if self._stack:
            self._stack.append((val, min(self._stack[-1][1], val)))
        else:
            self._stack.append((val, val))

    def pop(self) -> None:
        el = self._stack.pop()

    def top(self) -> int:
        return self._stack[-1][0]

    def getMin(self) -> int:
        return self._stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()