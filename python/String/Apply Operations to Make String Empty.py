from collections import Counter

class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        counts = Counter(reversed(s))
        
        max_count = max(counts.values())
        
        last_chars = [char for char in reversed(counts) if counts[char] == max_count]
        
        return "".join(last_chars)


solver = Solution()
result = solver.lastNonEmptyString("aabcbbca")
print(result)
