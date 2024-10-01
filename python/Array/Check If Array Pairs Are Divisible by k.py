from collections import Counter
from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # Calculate remainders and their frequencies
        remainder_count = Counter(x % k for x in arr)
        
        # Check if the number of elements with remainder 0 is even
        if remainder_count[0] % 2 != 0 :
            return False
        
        # Check for each remainder if it has a corresponding remainder that sums to k
        for r in list(remainder_count):
            if r == 0:
                continue
            complement = (k - r) % k
            if remainder_count[r] != remainder_count.get(complement, 0):
                return False
        
        return True
    
sol = Solution()
print(sol.canArrange(arr = [1,2,3,4,5,10,6,7,8,9], k = 5))
# print(sol.canArrange())