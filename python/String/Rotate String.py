class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        # Concatenate s with itself to form all possible rotations
        doubled_s = s + s
        
        return goal in doubled_s

sol =Solution()
print(sol.rotateString(s = "abcde", goal = "cdeab"))