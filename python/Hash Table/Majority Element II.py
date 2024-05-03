from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        res=[]
        mid = len(nums)/3
        for k,v in cnt.items():
            if v>mid:
                res.append(k)
        return res

s = Solution()

print(s.majorityElement([1]))
