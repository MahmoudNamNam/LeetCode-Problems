from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        key=-1
        nums_set= set(nums)
        for i in nums_set:
            if i >0:
                if i>key and -i in nums_set:
                    key =i
        return key
s = Solution()
print(s.findMaxK([-1,10,6,7,-7,1]))