from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        cnt=0
        l,r=0,len(nums)-1
        while l <r:
            if  nums[l] + nums[r] ==k :
                cnt+=1
                l +=1
                r-=1
            elif nums[l]+nums[r] <k:
                    l+=1
            else:
                    r-=1
        return cnt

s= Solution()
# print(s.maxOperations( nums = [1,2,3,4], k = 5))
# print)
print(s.maxOperations( nums = [3,1,3,4,3], k = 6))