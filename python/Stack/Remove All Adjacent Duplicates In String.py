class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            # Check if the stack is not empty and the top element is the same as the current character
            if stack and stack[-1] == c:
                stack.pop()  # Remove the duplicate
            else:
                stack.append(c)  # Append the current character if no duplicate
        return ''.join(stack)  

sol =Solution()
print(sol.removeDuplicates(s = "azxxzy"))
print(sol.removeDuplicates(s = "abbaca"))