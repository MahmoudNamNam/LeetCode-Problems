

from itertools import product
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Given a string containing digits 2-9, returns all possible letter combinations
        corresponding to the phone number represented by the digits, using itertools.product.

        Args:
            digits: A string containing digits 2-9.

        Returns:
            A list of strings representing all possible letter combinations.
            Returns an empty list if the input string is empty.
        """

        if not digits:  # Handle empty input string
            return []

        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        combinations_list = []
        for combination in product(*(digit_to_letters[d] for d in digits)):
            combinations_list.append(''.join(combination))

        return combinations_list

# Example usage
digits = "23"
solution = Solution()
combinations = solution.letterCombinations(digits)
print(combinations)  # Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
