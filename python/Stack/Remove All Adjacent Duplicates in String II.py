class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack =  [['$', 0]]     # a placeholder to mark stack is empty. This eliminates the need to do an empty check later
        
        for c in s:
            # If the top character matches the current character
            if stack[-1][0] == c:
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



"""
I have initialzed the stack with ['$', 0] placeholder. 
I am using ``$`` because the input string will only have lower case alphabets. I did this to remove the stack empty check. 

"""