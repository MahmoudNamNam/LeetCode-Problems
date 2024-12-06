from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        cnt =0
        total_sum =0
        for i in range(1, n + 1):
            if i in banned:
                continue
            total_sum+=i
            if total_sum > maxSum:
                return cnt
            cnt+=1
        
        return cnt
    
