from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        cumulative_shift = 0  # Initialize cumulative shift
        res = []
        
        # Traverse the string in reverse
        for i in range(n - 1, -1, -1):
            cumulative_shift += shifts[i]  # Add current shift to cumulative shift
            # Calculate new character after applying the cumulative shift
            new_char = chr(((ord(s[i]) - ord('a') + cumulative_shift) % 26) + ord('a'))
            res.append(new_char)
        
        # The result list will have characters in reverse order, so reverse it
        return ''.join(res[::-1])
