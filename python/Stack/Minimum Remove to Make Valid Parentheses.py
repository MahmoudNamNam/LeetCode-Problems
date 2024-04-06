class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        to_remove = set()

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if not stack:
                    to_remove.add(i)
                else:
                    stack.pop()

        to_remove.update(stack)  # Add unmatched '('

        result = ""
        for i, char in enumerate(s):
            if i not in to_remove:
                result += char

        return result

s = Solution()
print(s.minRemoveToMakeValid("lee(t(c)o)de)"))