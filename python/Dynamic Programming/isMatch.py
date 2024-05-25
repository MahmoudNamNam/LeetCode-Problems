class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        dp[0][0] = True
        
        # Only '*' can match with an empty string
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # '*' can either match no characters or one more character in s
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    # '?' matches any single character or characters must be the same
                    dp[i][j] = dp[i - 1][j - 1]
        
        return dp[m][n]

# Example usage:
sol = Solution()
print(sol.isMatch("aa", "a"))            # False
print(sol.isMatch("aa", "*"))            # True
print(sol.isMatch("cb", "?a"))           # False
print(sol.isMatch("adceb", "*a*b"))      # True
sol.isMatch("acdcb", "a*c?b")     # False
