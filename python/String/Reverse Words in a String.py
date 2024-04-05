class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()  # Split the string by whitespace into words
        reversed_words = words[::-1]  # Reverse the order of words
        return ' '.join(reversed_words)  # Join the reversed words with single spaces



solution = Solution()
print(solution.reverseWords("the sky is blue"))  # Output: "blue is sky the"
print(solution.reverseWords("  hello world  "))  # Output: "world hello"
print(solution.reverseWords("a good   example"))  # Output: "example good a"
