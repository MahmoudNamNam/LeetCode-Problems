from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        sm = sum(nums)
        left_side=0
        for i in range(len(nums)):
            left_side+=nums[i]
            right_side = sm-left_side
            if left_side -nums[i] == right_side: 
                return i 
        return -1

sol = Solution()
print(sol.findMiddleIndex([2,3,-1,8,4]))