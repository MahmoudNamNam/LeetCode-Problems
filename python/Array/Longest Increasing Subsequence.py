from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # This will store the smallest tail of all increasing subsequences
        tails = []

        for num in nums:
            # Find the index of the smallest number >= num
            idx = bisect.bisect_left(tails, num)
            # If num is larger than any element in tails, append it
            if idx == len(tails):
                tails.append(num)
            else:
                # Otherwise, replace the found index with num
                tails[idx] = num

        return len(tails)
