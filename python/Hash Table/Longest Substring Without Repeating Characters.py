class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        start = 0
        seen = {}  # Dictionary to track the last index of each character
        for i in range(len(s)):
            if s[i] in seen and seen[s[i]] >= start:  # Update start if the character is seen in the current window
                start = seen[s[i]] + 1
            seen[s[i]] = i  # Update the last index of the character
            max_count = max(max_count, i - start + 1)  # Calculate the length of the current substring
        return max_count

sol = Solution()
print(sol.lengthOfLongestSubstring("pwwkew"))  # Output: 3
