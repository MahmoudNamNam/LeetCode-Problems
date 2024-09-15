class MinStack:
    def __init__(self):
        self.stack = []      # Main stack to store all elements
        self.min_stack = []  # Auxiliary stack to store the minimum elements

    def push(self, val: int) -> None:
        self.stack.append(val)  # Add the value to the main stack
        
        # Add to the min_stack only if it is empty or the current value is smaller than or equal to the current minimum
        if len(self.min_stack) == 0 or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if len(self.stack) == 0:
            return None  # Stack is empty, no element to pop
        
        # Pop from the main stack
        top_element = self.stack.pop()
        
        # If the top element is the minimum, pop it from the min_stack as well
        if top_element == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return None  # Stack is empty, no top element
        return self.stack[-1]  # Return the top element of the main stack

    def getMin(self) -> int:
        if len(self.min_stack) == 0:
            return None  # Stack is empty, no minimum element
        return self.min_stack[-1]  # Return the top element of the min_stack, which is the minimum

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
