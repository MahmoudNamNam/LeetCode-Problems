from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count the frequency of each character in ransomNote and magazine
        ransomNoteCount = Counter(ransomNote)
        magazineCount = Counter(magazine)
        
        # Check if each character in ransomNote can be constructed from magazine
        for char, count in ransomNoteCount.items():
            if magazineCount[char] < count:
                return False
        
        return True

# Example usage:
sol = Solution()
print(sol.canConstruct("a", "b"))       # Output: False
print(sol.canConstruct("aa", "ab"))     # Output: False
print(sol.canConstruct("aa", "aab"))    # Output: True
