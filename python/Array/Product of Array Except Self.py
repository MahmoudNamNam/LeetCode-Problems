from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        total_product = 1
        for i in range(len(nums)):
            res[i] = total_product
            total_product *= nums[i]
        
        right_product = 1
        for i in reversed(range(len(nums))):
            res[i] *= right_product
            right_product *= nums[i]
            
        return res  


solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]