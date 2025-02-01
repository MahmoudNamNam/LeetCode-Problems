from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        for i in range(len(nums)-1):
            if (nums[i] % 2) == (nums[i+1] % 2):
                return False
        return True


sol = Solution()
print(sol.isArraySpecial([2, 7, 4, 9, 6, 1, 6, 3])) # True
print(sol.isArraySpecial([2, 7, 4, 9, 6, 1, 6, 6])) # False