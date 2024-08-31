from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        res=0
        min_distance=float('inf')

        for i in range(n):
            left =i+1
            right = n-1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right] 
                current_distance = abs(current_sum - target)
                if current_distance < min_distance:
                    min_distance = current_distance
                    res = current_sum
                if current_sum <target:
                    left +=1
                else:
                    right -=1
        return res