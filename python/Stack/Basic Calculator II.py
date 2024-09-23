class Solution:
    def precedence(self, op):
        # Dictionary lookup is faster than multiple condition checks
        precedences = {'+': 1, '-': 1, '*': 2, '/': 2}
        return precedences.get(op, 0)

    def get_tokens(self, s):
        tokens = []
        operators = []
        num = ""
        for i in range(len(s)):
            if s[i].isdigit():
                num += s[i] # Collect digits for multi-digit numbers
            else:
                if num:
                    tokens.append(num)
                    num = ""
                if s[i] == ' ':
                    continue # Skip spaces
                else:
                    # Pop operators with higher or equal precedence
                    while operators and self.precedence(operators[-1]) >= self.precedence(s[i]):
                        tokens.append(operators.pop())
                    operators.append(s[i])
        if num:
            tokens.append(num)
        while operators:
            tokens.append(operators.pop())
        return tokens

    def calculate(self, s: str) -> int:
        stack = []
        tokens = self.get_tokens(s)
        for token in tokens:
            if token in '+-*/':
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(int(a / b)) 
            else:
                stack.append(int(token))
        return stack[0]


sol = Solution()
s = "3+2*2"
print(sol.get_tokens(s))
print(sol.calculate(s))

s = " 3/2 "
print(sol.get_tokens(s))
print(sol.calculate(s))

s = " 3+5 / 2 "
print(sol.get_tokens(s))
print(sol.calculate(s))
