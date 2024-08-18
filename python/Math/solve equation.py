class Solution:
    def solveEquation(self, equation: str) -> str:
        
        def parse_expression(expr):
            """
            Helper function to parse the expression on either side of the equation.
            It returns the sum of coefficients of 'x' and the sum of constant terms.
            """
            coeff, const = 0, 0  # Initialize the coefficient and constant sums
            num, sign = 0, 1  # `num` stores the current number, `sign` is either 1 (positive) or -1 (negative)
            i = 0  # Start index for traversing the string
            
            while i < len(expr):  # Loop through the expression
                if expr[i] == '+':
                    sign = 1  # Positive sign found
                    i += 1
                elif expr[i] == '-':
                    sign = -1  # Negative sign found
                    i += 1
                elif expr[i].isdigit():  # If the current character is a digit
                    num = 0
                    while i < len(expr) and expr[i].isdigit():  # Read the whole number
                        num = num * 10 + int(expr[i])
                        i += 1
                    if i < len(expr) and expr[i] == 'x':  # Check if the number is a coefficient for 'x'
                        coeff += sign * num  # Add the coefficient to the sum
                        i += 1  # Move past the 'x'
                    else:
                        const += sign * num  # If it's not attached to 'x', add it to the constant sum
                elif expr[i] == 'x':  # If the character is 'x' without an explicit number
                    coeff += sign  # The coefficient is 1 or -1 depending on the sign
                    i += 1
                else:
                    i += 1  # Move past any other characters (though there shouldn't be any)
            
            return coeff, const  # Return the combined coefficient and constant
    
        # Split the equation into the left-hand side and right-hand side
        left, right = equation.split('=')
        
        # Parse both sides of the equation to get coefficients and constants
        left_coeff, left_const = parse_expression(left)
        right_coeff, right_const = parse_expression(right)
        
        # Calculate the final coefficient and constant by moving everything to the left-hand side
        final_coeff = left_coeff - right_coeff
        final_const = right_const - left_const
        
        # Determine the type of solution based on the simplified equation
        if final_coeff == 0:  # If the coefficient of 'x' is 0
            if final_const == 0:
                return "Infinite solutions"  # If both are zero, the equation holds for any 'x'
            else:
                return "No solution"  # If the constant is non-zero, the equation is impossible
        else:
            return f'x={final_const // final_coeff}'  # Solve for 'x' and return the result

# Example cases
solver = Solution()
print(solver.solveEquation("x+5-3+x=6+x-2"))  # Output: "x=2"
print(solver.solveEquation("x=x"))  # Output: "Infinite solutions"
print(solver.solveEquation("2x=x"))  # Output: "x=0"
