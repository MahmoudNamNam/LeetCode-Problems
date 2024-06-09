from typing import List
from collections import defaultdict
from itertools import accumulate

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_count = defaultdict(int)
        remainder_count[0] = 1
        result = 0
        
        for prefix_sum in accumulate(nums):
            remainder = prefix_sum % k
            result += remainder_count[remainder]
            remainder_count[remainder] += 1
            
        return result


sol = Solution()
nums = [4,5,0,-2,-3,1]
k = 5
print(sol.subarraysDivByK(nums, k))

nums = [5]
k = 9
print(sol.subarraysDivByK(nums, k))