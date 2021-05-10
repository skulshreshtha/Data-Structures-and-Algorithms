class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._data = []     # Using list to represent stack

    def push(self, val: int) -> None:
        """
        Push a new element to the stack
        """
        if not self._data:
            new_min = val
        else:
            top = self._data[-1]
            new_min = min(val, top[1])        
        self._data.append((val,new_min))

    def pop(self) -> None:
        """
        Remove the top element from stack. No return.
        """
        if not self._data:
            return None
        del self._data[-1]

    def top(self) -> int:
        """
        Return the top element from stack. Not Remove.
        """
        if not self._data:
            return None
        top = self._data[-1]
        return top[0]

    def getMin(self) -> int:
        """
        Return the current minimum element from stack.
        """
        if not self._data:
            return None
        return self._data[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()