from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        cnt = 0
        current_length = 0
        
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                current_length += 1
                cnt += current_length
            else:
                current_length = 0
        
        return cnt



sol =Solution()

nums = [1,2,3,4]
print( sol.numberOfArithmeticSlices(nums))