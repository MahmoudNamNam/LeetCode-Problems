from typing import List

class Solution:
    def no_common_letters(self, word1: str, word2: str) -> bool:
        # Convert words to sets of characters
        set1 = set(word1)
        set2 = set(word2)
        # Check if intersection is empty
        return set1.isdisjoint(set2)

    def maxProduct(self, words: List[str]) -> int:
        max_product = 0
        n = len(words)
        # Compare all pairs of words
        for i in range(n):
            for j in range(i + 1, n):
                if self.no_common_letters(words[i], words[j]):
                    product = len(words[i]) * len(words[j])
                    if product > max_product:
                        max_product = product
        return max_product

sol = Solution()
print(sol.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))
print(sol.maxProduct(["a","ab","abc","d","cd","bcd","abcd"]))
print(sol.maxProduct(["a","aa","aaa","aaaa"]))

from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # Create a list of tuples where each tuple contains the bitmask and the length of the word
        word_info = []
        
        for word in words:
            bitmask = 0
            for char in word:
                bitmask |= 1 << (ord(char) - ord('a'))
            word_info.append((bitmask, len(word)))
        
        max_product = 0
        n = len(words)
        
        # Compare all pairs of words
        for i in range(n):
            for j in range(i + 1, n):
                if word_info[i][0] & word_info[j][0] == 0:  # No common letters
                    product = word_info[i][1] * word_info[j][1]
                    max_product = max(max_product, product)
        
        return max_product

# Example usage
solution = Solution()
words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
result = solution.maxProduct(words)
print(f"The maximum product of lengths of two words with no common letters is: {result}")
