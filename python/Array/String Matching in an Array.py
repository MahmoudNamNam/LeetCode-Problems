from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    result.append(words[i])
                    break
        return result


sol = Solution()

words1 = ["mass", "as", "hero", "superhero"]
words2 = ["leetcode", "et", "code"]
words3 = ["blue", "green", "bu"]

print(sol.stringMatching(words1))  # Output: ["as", "hero"]
print(sol.stringMatching(words2))  # Output: ["et", "code"]
print(sol.stringMatching(words3))  # Output: []