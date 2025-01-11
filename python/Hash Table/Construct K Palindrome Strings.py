from collections import Counter
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:

        freq = Counter(s)
        odd_count = sum(1 for count in freq.values() if count % 2 == 1)
        return odd_count <= k <= len(s)
    

sol = Solution()

print(sol.canConstruct("annabelle", 2)) # True
print(sol.canConstruct("leetcode", 3)) # False      