class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        start = 0
        current_cost = 0
        max_length = 0

        for i in range(n):
            current_cost += abs(ord(s[i]) - ord(t[i]))

            while current_cost > maxCost:
                current_cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1

            max_length = max(max_length, i - start + 1)
        
        return max_length
    



sol = Solution()

print(sol.equalSubstring(s = "abcd", t = "bcdf", maxCost = 3))
print(sol.equalSubstring(s = "abcd", t = "cdef", maxCost = 3))
print(sol.equalSubstring(s = "abcd", t = "acde", maxCost = 0))