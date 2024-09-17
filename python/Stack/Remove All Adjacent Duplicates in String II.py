class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for c in s:
            # If stack is not empty and the top character matches the current character
            if stack and stack[-1][0] == c:
                # Increment the count of the top character
                stack[-1] = (c, stack[-1][1] + 1)
                # If the count reaches k, pop the character from the stack
                if stack[-1][1] == k:
                    stack.pop()
            else:
                # Push the character and set its count to 1
                stack.append((c, 1))
        
        # Rebuild the string by repeating each character according to its count
        return ''.join(c * count for c, count in stack)

sol =Solution()
print(sol.removeDuplicates(s = "abcd", k = 2))
print(sol.removeDuplicates(s = "deeedbbcccbdaa", k = 3))