from collections import Counter
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return list(words[0])

        # Initialize the counter with the frequency of characters in the first word
        common_counter = Counter(words[0])
        # Update the counter with the minimum frequency of characters found in subsequent words
        for word in words[1:]:
            word_counter = Counter(word)
            for char in list(common_counter):
                if char in word_counter:
                    common_counter[char] = min(common_counter[char], word_counter[char])
                else:
                    del common_counter[char]

        # Collect the characters based on their frequency in the common_counter
        result = []
        for char, freq in common_counter.items():
            result.extend([char] * freq)

        return result

sol =Solution()
words = ["bella","label","roller"]
print(sol.commonChars(words))

words = ["cool","lock","cook"]
print(sol.commonChars(words))