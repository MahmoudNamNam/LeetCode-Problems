from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        indexed_scores = [(s, i) for i, s in enumerate(score)]
        
        indexed_scores.sort(reverse=True, key=lambda x: x[0])
        
        rank_names = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        
        answer = [""] * len(score)
        
        for rank, (_, index) in enumerate(indexed_scores[:3]):
            answer[index] = rank_names[rank]
        
        for rank, (_, index) in enumerate(indexed_scores[3:], start=4):
            answer[index] = str(rank)
        
        return answer



s = Solution()

s.findRelativeRanks([10,3,8,9,4])