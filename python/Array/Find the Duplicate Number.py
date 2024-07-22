class Solution:
    def findDuplicate(self, nums) -> int:
        seen = {}
        for i in nums:
            if i in seen:
                return i
            seen[i] = True  
