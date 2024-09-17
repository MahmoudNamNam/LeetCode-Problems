class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for p in s:
            if p in parentheses:  # opening bracket
                stack.append(p)
            else:  #closing bracket
                if not stack or parentheses[stack.pop()] != p:
                    return False

        return len(stack) == 0
