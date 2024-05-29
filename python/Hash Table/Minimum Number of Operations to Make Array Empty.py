from collections import Counter
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        cnt=0
        
        for _,value in counter.items():
            if value ==1:
                return -1
            cnt+=(value//3)
            if value%3==2 or value%3==1:
                cnt+=1
        return  cnt


sol =Solution()
print(sol.minOperations( [2,3,3,2,2,4,2,3,4]))
print(sol.minOperations([2,1,2,2,3,3]))