from collections import defaultdict

class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        for length in range(n, 0, -1):
            substring_count = defaultdict(int)
            for i in range(n - length + 1):
                sub = s[i:i+length]
                if len(set(sub)) == 1:
                    substring_count[sub] += 1
            for count in substring_count.values():
                if count >= 3:
                    return length
        return -1

sol = Solution()
print(sol.maximumLength(s = "abcdef"))
print(sol.maximumLength(s = "abcaba"))