from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Memoization dictionary to store results of sub-expressions
        memo = {}
        
        def helper(expr):
            # If result for this expression is already calculated, return it
            if expr in memo:
                return memo[expr]
            
            # Store results for current expression
            result = []
            
            # Split the expression at each operator
            for i in range(len(expr)):
                if expr[i] in "+-*":
                    # Recursively calculate the result of left and right parts
                    left = helper(expr[:i])
                    right = helper(expr[i+1:])
                    
                    # Combine the results of left and right based on the current operator
                    for l in left:
                        for r in right:
                            if expr[i] == '+':
                                result.append(l + r)
                            elif expr[i] == '-':
                                result.append(l - r)
                            elif expr[i] == '*':
                                result.append(l * r)
            
            # If the result list is still empty, the expression is just a number
            if not result:
                result.append(int(expr))
            
            # Memoize the result for the current expression
            memo[expr] = result
            return result
        
        # Start the recursion with the full expression
        return helper(expression)

# Test cases
expression1 = "2-1-1"
expression2 = "2*3-4*5"
sol = Solution()
print(sol.diffWaysToCompute(expression1))  # Output: [0, 2]
print(sol.diffWaysToCompute(expression2))  # Output: [-34, -14, -10, -10, 10]
