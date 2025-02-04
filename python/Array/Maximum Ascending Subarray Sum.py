from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        max_sum = nums[0]
        current_sum = nums[0]
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                current_sum += nums[i]
            else:
                current_sum = nums[i]
            max_sum = max(max_sum, current_sum)
        return max_sum

sol=Solution()
print(sol.maxAscendingSum([10,20,30,5,10,50])) # 65

print(sol.maxAscendingSum([10,20,30,40,50])) # 150

