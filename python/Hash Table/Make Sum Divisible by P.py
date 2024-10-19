from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        remainder = total_sum % p
        
        if remainder == 0:
            return 0  # Already divisible by p


        prefix_sum = 0
        remainder_map = {0: -1}
        n=len(nums)
        mn_len = n
        
        for i, num in enumerate(nums):
            prefix_sum += num
            current_prefix_mod = prefix_sum % p
            
            # The target remainder we need to remove to make sum divisible by p
            target_mod = (current_prefix_mod - remainder) % p
            
            # Check if this target exists in the hash map
            if target_mod in remainder_map:
                sub_len = i - remainder_map[target_mod]
                mn_len = min(mn_len, sub_len)
            
            # Update hash map with the current prefix sum modulo p
            remainder_map[current_prefix_mod] = i
        
        return mn_len if mn_len != n else -1



sol = Solution()
print(sol.minSubarray(nums = [3,1,4,2], p = 6))
print(sol.minSubarray(nums = [4,4,2], p = 7))
print(sol.minSubarray(nums = [1,2,3], p = 7))