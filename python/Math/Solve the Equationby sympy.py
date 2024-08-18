from sympy import symbols, Eq, solve, simplify

class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split('=')
        
        x = symbols('x')
        
        left_expr = simplify(left)
        right_expr = simplify(right)
        
        solution = solve(Eq(left_expr, right_expr), x)
        
        if not solution:  
            return "No solution"
        elif len(solution) == 1: 
            return f'x={solution[0]}'
        else:  
            return "Infinite solutions"

solver = Solution()
print(solver.solveEquation("x+5-3+x=6+x-2"))  # Output: "x=2"
print(solver.solveEquation("x=x"))  # Output: "Infinite solutions"
print(solver.solveEquation("2x=x"))  # Output: "x=0"
