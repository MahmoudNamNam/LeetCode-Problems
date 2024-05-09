from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        happinessScore = 0
        for i in range(min(k, len(happiness))):
            happinessScore += max(0, happiness[i] - i)
        return happinessScore



s = Solution()

s.maximumHappinessSum(happiness = [2,3,4,5], k = 1)