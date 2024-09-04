from itertools import accumulate
from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        mn_ele = prefix[0]
        
        for i in range(1, n):
            prefix[i] = nums[i] + prefix[i-1]
            mn_ele = min(mn_ele, prefix[i])
        
        # If mn_ele is negative, the start value should be at least 1 - mn_ele
        return max(1 - mn_ele, 1)



sol = Solution()

print(sol.minStartValue([-3,2,-3,4,2]))
print(sol.minStartValue([1,-2,-3]))




class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        return max(1, 1 - min(accumulate(nums)))