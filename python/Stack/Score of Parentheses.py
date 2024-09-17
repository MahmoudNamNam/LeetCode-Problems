class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0] 
        
        for char in s:
            if char == '(':
                # Start a new level in the stack
                stack.append(0)
            else: 
                # End the current level
                top = stack.pop()
                # Check if we are closing a pair "()", which contributes a score of 1
                if top == 0:
                    score = 1
                else:
                    # If we are closing "(A)", the score is 2 * A
                    score = 2 * top
                # Add the score to the previous level in the stack
                stack[-1] += score
        
        # The final score is the only element left in the stack
        return stack[0]

sol = Solution()

print(sol.scoreOfParentheses(s = "()"))
print(sol.scoreOfParentheses(s = "(()(()))"))
