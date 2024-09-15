from typing import Counter, List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        cnt =Counter(nums)
        lst=[]
        for key,val in cnt.items():
            if val >1:
                lst.append(key)
        return lst