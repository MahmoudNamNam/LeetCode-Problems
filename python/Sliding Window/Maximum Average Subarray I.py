from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sm=0
        for i in range(k):
            sm+= nums[i]
        max_sm=sm
        for i in range(k,len(nums)):
            sm+=nums[i]
            sm-=nums[i-k]
            max_sm = max(max_sm,sm)
        return max_sm /k

sol = Solution()
print(sol.findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4))
print(sol.findMaxAverage(nums = [5], k = 1))
