from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift_values = [0] * (n + 1)

        # Record the shift operations
        for start, end, direction in shifts:
            if direction == 1:  # Forward shift
                shift_values[start] += 1
                shift_values[end + 1] -= 1
            else:  # Backward shift
                shift_values[start] -= 1
                shift_values[end + 1] += 1

        # Compute the cumulative shift for each character
        for i in range(1, n):
            shift_values[i] += shift_values[i - 1]

        # Apply shifts to the string
        result = []
        for i, char in enumerate(s):
            shift = shift_values[i]
            # Calculate the new character
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result.append(new_char)

        return ''.join(result)

sol =Solution()
print(sol.shiftingLetters(s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]) ) #"ace"