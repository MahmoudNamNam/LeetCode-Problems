class Solution:
    def countSubstrings(self, s: str) -> int:
        # Length of the string
        n = len(s)
        
        # Counter for palindromic substrings
        cnt = 0
        
        # Helper function to expand around the center and count palindromes
        def expandAroundCenter(left, right):
            nonlocal cnt  # Allows us to modify the outer scope variable 'cnt'
            while left >= 0 and right < n and s[left] == s[right]:
                # Increment the counter for each palindrome found
                cnt += 1
                # Expand outwards
                left -= 1
                right += 1

        # Iterate through each character in the string
        for i in range(n):
            # Consider odd-length palindromes centered at s[i]
            expandAroundCenter(i, i)
            # Consider even-length palindromes centered between s[i] and s[i + 1]
            expandAroundCenter(i, i + 1)
        
        # Return the total count of palindromic substrings
        return cnt

sol = Solution()

# Test cases
print(sol.countSubstrings("abc"))  # Output: 3 (a, b, c)
print(sol.countSubstrings("aaa"))  # Output: 6 (a, a, a, aa, aa, aaa)
