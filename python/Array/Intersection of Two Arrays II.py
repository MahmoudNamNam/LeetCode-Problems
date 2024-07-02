from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_cnt = Counter(nums1)
        result=[]
        for num in nums2:
            if num1_cnt[num] > 0:
                result.append(num)
                num1_cnt[num]-=1
        return result
    

sol = Solution()
print(sol.intersect([1,2,2,1], [2,2]))        # Output: [2, 2]
print(sol.intersect([4,9,5], [9,4,9,8,4]))    # Output: [4, 9]