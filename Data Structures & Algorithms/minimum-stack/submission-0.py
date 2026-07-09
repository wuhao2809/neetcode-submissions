from collections import deque
class MinStack:

    def __init__(self):
        self.mono = deque()
        self.stack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mono or self.mono[-1] >= val:
            self.mono.append(val)

    def pop(self) -> None:
        curr = self.stack.pop()
        if curr == self.mono[-1]:
            self.mono.pop()


    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        # maintain a monotonic increasing queue
        return self.mono[-1]
        
