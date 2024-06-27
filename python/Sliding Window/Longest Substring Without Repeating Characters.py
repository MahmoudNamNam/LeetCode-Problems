class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(set(s)) == 1:  # Special case for strings with only one unique character
            return 1
        max_count = 0
        current_count = 0
        start = 0
        seen = set()  # Set to track characters in the current substring
        for i in range(len(s)):
            while s[i] in seen:  # Remove characters from the start until s[i] is not in the set
                seen.remove(s[start])
                current_count -= 1
                start += 1
            seen.add(s[i])  # Add the current character to the set
            current_count += 1  # Increment the count of the current substring length
            max_count = max(max_count, current_count)  # Update max_count if the current substring is longer
        return max_count

sol = Solution()
print(sol.lengthOfLongestSubstring("pwwkew"))  # Output: 3

