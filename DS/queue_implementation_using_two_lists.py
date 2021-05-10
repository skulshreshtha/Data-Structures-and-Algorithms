class MyQueue(object):
    def __init__(self):
        """ Creates two empty stacks for implementing the queue (FIFO)."""
        self._front_stack = []
        self._back_stack = [] 
    
    def peek(self):
        """ Returns (without removing) the element at front of the queue."""
        self._prepare_stacks()
        return self._front_stack[-1]
        
    def pop(self):
        """ Returns and removes the element at front of the queue."""
        self._prepare_stacks()
        return self._front_stack.pop()
        
    def put(self, value):
        """ Adds element to the back of the queue."""
        self._back_stack.append(value)
        
    def _prepare_stacks(self):
        """ Move all elements from back stack to front stack for peek and pop."""
        if(len(self._front_stack) == 0):
            while(len(self._back_stack) > 0):
                self._front_stack.append(self._back_stack.pop())

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())