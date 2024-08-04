from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod=10**9 +7
        sub=[]
        for start in range(n):
            current_sum = 0  
            for end in range(start, n):
                current_sum += nums[end]  # Add current element to the sum
                # Add this subarray sum to the list of sums
                sub.append(current_sum)
        sub.sort()
          
        return sum(sub[left-1:right]) % mod

