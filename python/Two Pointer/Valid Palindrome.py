class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s) - 1

        while left < right:
            # Move left pointer to the next alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1
            # Move right pointer to the previous alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1
            # Compare characters
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True


sol =Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))


""""
Use isalnum(): Checks both letters and digits, which is typically what's expected for a palindrome check.
Use isalpha(): Only checks letters, so it would incorrectly ignore digits, which could lead to wrong results in cases where digits are involved in the palindrome check.
"""