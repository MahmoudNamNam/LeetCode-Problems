from collections import Counter
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        for v in cnt.values():
            if v >1:
                return True
        return False


sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen =set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums))!=len(nums)