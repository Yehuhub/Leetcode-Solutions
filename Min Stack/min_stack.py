
class MinStack:

    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else: 
            self.min_stack.append(val)

    def pop(self) -> None:
        self.main_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        if self.main_stack:
            return self.main_stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]        
        
