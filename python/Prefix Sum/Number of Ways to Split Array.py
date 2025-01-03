from typing import List


# class Solution:
#     def waysToSplitArray(self, nums: List[int]) -> int:
#         cnt =0
#         for i in range(1,len(nums)):
#             if sum(nums[:i])>=sum(nums[i:]):
#                 cnt += 1
#         return cnt
        
#  O(N^2)


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        # Compute the prefix sums
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
        
        total_sum = prefix_sum[-1]
        valid_splits = 0
        
        # Check each possible split index
        for i in range(n - 1):
            left_sum = prefix_sum[i]
            right_sum = total_sum - left_sum
            if left_sum >= right_sum:
                valid_splits += 1
        
        return valid_splits
# O(N)



from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        right_sum = sum(nums)
        left_sum = 0
        valid_splits = 0
        
        for i in range(n - 1):
            left_sum += nums[i]
            right_sum -= nums[i]
            if left_sum >= right_sum:
                valid_splits += 1
        
        return valid_splits
