from collections import Counter
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res=[]
        counter=Counter(nums)
        for key,value in counter.items():
            if value ==1:
                res.append(key)
        return res
    
sol =Solution()

print(sol.singleNumber([1,2,1,3,2,5]))