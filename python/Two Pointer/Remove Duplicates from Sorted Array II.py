from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r=0,0
        n=len(nums)
        while r < n:
            cnt=1
            while r+1 < n and nums[r] == nums[r+1]:
                r+=1
                cnt+=1
            for i in range(min(cnt,2)):
                nums[l]=nums[r]
                l+=1
            r+=1
        return l



