from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        
        if total_sum % k != 0:
            return False
        
        target_sum = total_sum // k
        
        nums.sort(reverse=True)
        
        if nums[0] > target_sum:
            return False
        
        subset_sums = [0] * k
        
        def backtrack(index):
            if index == len(nums):
                return all(subset_sum == target_sum for subset_sum in subset_sums)
            
            num = nums[index]
            
            for i in range(k):
                if subset_sums[i] + num <= target_sum:
                    subset_sums[i] += num
                    
                    if backtrack(index + 1):
                        return True
                    
                    subset_sums[i] -= num
                
                if subset_sums[i] == 0:
                    break
            
            return False
        
        return backtrack(0)
sol = Solution()
    # Example usage
print(sol.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))  # Output: True
print(sol.canPartitionKSubsets([1, 2, 3, 4], 3))            # Output: False
