class Solution:
    def gcd(self,a, b):
        """
        Calculates the greatest common divisor of two numbers using the Euclidean algorithm.
        """
        while b:
            a, b = b, a % b
        return a
    
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        Finds the largest string that divides both str1 and str2.

        Args:
            str1 (str): The first string.
            str2 (str): The second string.

        Returns:
            str: The largest string x such that x divides both str1 and str2.
                 Returns an empty string if no such string exists.

        Example:
            >>> solution = Solution()
            >>> solution.gcdOfStrings("ABCABC", "ABC")
            'ABC'
            >>> solution.gcdOfStrings("ABABAB", "ABAB")
            'AB'
            >>> solution.gcdOfStrings("LEET", "CODE")
            ''

        Complexity Analysis:
            - Time complexity: O(n + m), where n and m are the lengths of str1 and str2, respectively.
              The time complexity is dominated by finding the greatest common divisor of the lengths
              of the input strings.
            - Space complexity: O(1), since the algorithm uses constant extra space.
        """

        if str1 + str2 != str2 + str1:
            return ""

        gcd_length = self.gcd(len(str1), len(str2))
        return str1[:gcd_length]

# Example usage:
solution = Solution()
str1 = "ABCABC"
str2 = "ABC"
print(solution.gcdOfStrings(str1, str2))  # Output: "ABC"

str1 = "ABABAB"
str2 = "ABAB"
print(solution.gcdOfStrings(str1, str2))  # Output: "AB"

str1 = "LEET"
str2 = "CODE"
print(solution.gcdOfStrings(str1, str2))  # Output: ""
