from collections import Counter
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_=max(nums)
        max_len=0
        cur_len=0
        for i in nums:
            if i==max_:
                cur_len+=1
            else:
                max_len=max(max_len,cur_len)
                cur_len=0
        max_len=max(max_len,cur_len)
        return max_len
