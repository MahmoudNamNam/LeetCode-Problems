import bisect
from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        
        n = len(nums)
        count = 0
        
        for i in range(n - 1):
            min_val = lower - nums[i]
            max_val = upper - nums[i]
            
            start = bisect.bisect_left(nums, min_val, i + 1, n)
            end = bisect.bisect_right(nums, max_val, i + 1, n) - 1
            
            if start <= end:
                count += end - start + 1
        
        return count
    
sol = Solution()
print(sol.countFairPairs(nums = [0,1,7,4,4,5], lower = 3, upper = 6))
print(sol.countFairPairs(nums = [1,7,9,2,5], lower = 11, upper = 11))