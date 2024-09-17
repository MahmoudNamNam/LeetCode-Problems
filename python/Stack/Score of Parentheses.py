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

"""
Consider: (()(()))
We know any valid sub-expression can be replaced with its value. Let's find smallest ones

( () ( () )) ==> ( 1+ ( () )) ==> ( 1 ( 1 )) ==> (1 + 2) ==> (3) ==> 6
We see that subexpressions () with value 1 and (()) with value 2 are part of a bigger expression (()(()))

We can write inefficient code to keep find internal small expressions, but can we do smarter?

Thinking in processing left to right: we either
- have ( to indicate a new subexpression that will have ) in future
- or ) to indicate there is a subexpression that is done now

Stack can help us to do that
- We find (, we add 0: it represents the initial sum of the internal subexpressions
- We find ), we finish a subexpression value and accumulate to its parent

It might now be easy to get idea, but its solution can be a similar thinking style in other stack problems


"""