class MinStack:

    def __init__(self):
        self.stack = []
        self.mintracker = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.mintracker or val <= self.mintracker[-1]:
            self.mintracker.append(val)

    def pop(self) -> None:
        val = self.stack.pop()

        if val == self.mintracker[-1]:
            self.mintracker.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mintracker[-1]
        
