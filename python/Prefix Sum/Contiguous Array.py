from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        max_len=0
        index ={0:-1}
        sm=0
        for i ,num in enumerate(nums):
            # Update cumulative sum: +1 for 1, -1 for 0
            sm +=1 if num else -1
            # If the cumulative sum has been seen before, calculate the subarray length
            if sm in index:
                max_len = max(max_len,i- index[sm])
            else:
                index[sm] = i
        return max_len
