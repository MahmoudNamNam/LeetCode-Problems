class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Check if lengths are equal
        if len(s) != len(goal):
            return False
        
        # Concatenate s with itself to form all possible rotations
        doubled_s = s + s
        
        # Check if goal is a substring of doubled_s
        return goal in doubled_s

sol =Solution()
print(sol.rotateString(s = "abcde", goal = "cdeab"))