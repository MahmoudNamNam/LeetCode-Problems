from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Count the frequency of each character in the string
        count = Counter(s)
        
        # Iterate through the string and find the first character with a frequency of 1
        for index, char in enumerate(s):
            if count[char] == 1:
                return index
        
        # Return -1 if no unique character is found
        return -1
