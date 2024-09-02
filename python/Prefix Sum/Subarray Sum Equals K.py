from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sm =0
        prefix = {0:1}
        for num in nums:
            sm += num
            diff = sm -k
            if diff in prefix:
                count += prefix[diff]
            if sm in prefix:
                prefix[sm]+=1
            else:
                prefix[sm]=1
        return count