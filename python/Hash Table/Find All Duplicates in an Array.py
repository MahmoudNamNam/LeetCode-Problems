
from collections import Counter
from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        res=[]
        for i,v in cnt.items():
            if v > 1:
                res.append(i)
        return res

s = Solution()

print(s.findDuplicates([4,3,2,7,8,2,3,1]))



class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        res = []
        for n in nums:
            if n in seen:
                res.append(n)
                continue
            seen.add(n)
        return res