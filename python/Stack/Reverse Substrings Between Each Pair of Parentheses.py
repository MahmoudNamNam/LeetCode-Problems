class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == ')':
                temp = []
                # Pop characters until we find the matching opening bracket '('
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                # Pop the opening bracket '('
                stack.pop()
                # Push the reversed substring back onto the stack
                stack.extend(temp)
            else:
                # Push current character to the stack
                stack.append(char)
        
        # Join all characters in the stack to form the final result
        return ''.join(stack)



class Solution:
    def reverseParentheses(self, s: str) -> str:
        # Initialize a stack with an empty string to store characters and reversed substrings
        st = ['']

        # Iterate through each character in the string s
        for char in s:
            if char == '(':
                # When encountering '(', start a new substring by appending an empty string to the stack
                st.append('')
            elif char == ')':
                # When encountering ')', pop the last substring from the stack, reverse it, and concatenate it to the previous substring
                reversed_chars = st.pop()[::-1]
                st[-1] += reversed_chars
            else:
                # If the character is a letter, append it to the last substring in the stack
                st[-1] += char

        # At the end of the iteration, return the final concatenated string from the stack
        return st.pop()

# Example usage
solution = Solution()
print(solution.reverseParentheses("(abcd)"))  # Output: "dcba"
print(solution.reverseParentheses("(u(love)i)"))  # Output: "iloveu"
print(solution.reverseParentheses("(ed(et(oc))el)"))  # Output: "leetcode"
