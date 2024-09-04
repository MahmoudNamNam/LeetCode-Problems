from typing import List



class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        # Step 1: Calculate postfix sums for shifts
        n = len(shifts)
        postfix_sums = [0] * n
        
        # Initialize the last element of postfix_sums
        postfix_sums[-1] = shifts[-1]
        
        # Fill the postfix_sums array with cumulative sums from the end to the start
        for i in range(n - 2, -1, -1):
            postfix_sums[i] = shifts[i] + postfix_sums[i + 1]
        
        # Step 2: Apply the calculated shifts to the string
        res = ''
        
        # Loop through each character in the string with its corresponding shift
        for char, shift in zip(s, postfix_sums):
            # Calculate the new character after applying the shift
            new_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            res += new_char  # Append the shifted character to the result string
        
        return res  # Return the final shifted string



sol = Solution()

print(sol.shiftingLetters(s = "abc", shifts = [3,5,9]))