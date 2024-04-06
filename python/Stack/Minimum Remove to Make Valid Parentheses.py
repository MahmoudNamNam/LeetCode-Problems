class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Removes the minimum number of parentheses to make the string valid.

        Args:
            s (str): The input string containing parentheses.

        Returns:
            str: The modified string with the minimum number of parentheses removed to make it valid.
        """
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