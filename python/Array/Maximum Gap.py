from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        mx_gap = 0
        for i in range(1, len(nums)):
            mx_gap=max(mx_gap,nums[i]-nums[i-1])
        return mx_gap