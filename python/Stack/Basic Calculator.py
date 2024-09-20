class Solution:
    def calculate(self, s: str) -> int:
        # Initialize the result, sign, and stack
        result = 0
        sign = 1  # 1 means positive, -1 means negative
        stack = []
        num = 0  # To build the numbers

        for ch in s:
            if ch.isdigit():
                # Build the current number
                num = num * 10 + int(ch)
            
            elif ch == '+':
                # Complete the previous number and add it to the result
                result += sign * num
                num = 0  # Reset the number
                sign = 1  # The next number should be added
            
            elif ch == '-':
                # Complete the previous number and add it to the result
                result += sign * num
                num = 0  # Reset the number
                sign = -1  # The next number should be subtracted
            
            elif ch == '(':
                # Push the current result and sign to the stack for later
                stack.append(result)
                stack.append(sign)
                # Reset result and sign for the new sub-expression
                result = 0
                sign = 1
            
            elif ch == ')':
                # Add the last number to result inside the parentheses
                result += sign * num
                num = 0
                # Pop the sign and the previous result from the stack
                result *= stack.pop()  # stack.pop() is the sign before the parenthesis
                result += stack.pop()  # stack.pop() is the result calculated before the parenthesis
            
            # We ignore spaces as they don't affect the calculation
        
        # After the loop, add any number left (in case the expression ends with a number)
        result += sign * num
        
        return result


s = "(1+(4+5+2)-3)+(6+8)"
sol = Solution()

print(sol.calculate(s))