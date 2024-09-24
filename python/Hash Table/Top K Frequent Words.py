from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        # Sort words by frequency first (-cnt[word]) and then alphabetically (word)
        sorted_words = sorted(cnt.keys(), key=lambda word: (-cnt[word], word))
        return sorted_words[:k]

# Test the solution
sol = Solution()
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 3
print(sol.topKFrequent(words, k))  # Expected: ["i", "love", "coding"]
