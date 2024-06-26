from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        
        return nums
s= Solution()
a =[0,1,0,3,12]
s.moveZeroes(a)
print(a)