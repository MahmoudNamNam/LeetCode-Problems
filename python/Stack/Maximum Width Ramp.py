from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        
        # Step 1: Build a decreasing stack of indices
        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
        maxWidth = 0
        
        # Step 2: Traverse from the end and find maximum width ramp
        for j in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                maxWidth = max(maxWidth, j - stack.pop())
            if not stack :break
        
        return maxWidth
    

sol =Solution()
print(sol.maxWidthRamp([6,0,8,2,1,5]))
print(sol.maxWidthRamp([9,8,1,0,1,9,4,0,4,1]))


