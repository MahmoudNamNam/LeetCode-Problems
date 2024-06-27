from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        current_sum = 0
        res=float('inf')
        for end in range(len(nums)):
            current_sum += nums[end]
            while current_sum >= target :
                res = min(res,end - start +1)
                current_sum -= nums[start]
                start +=1
        return res if res != float('inf') else 0

sol =Solution()
target = 7
nums = [2,3,1,2,4,3]
print(sol.minSubArrayLen(target, nums)) #The subarray [4,3] has the minimal length under the problem constraint.

target = 11
nums = [1,1,1,1,1,1,1,1]
print(sol.minSubArrayLen(target, nums)) #0