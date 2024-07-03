from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []  # This will store the resulting list of triplets
        nums.sort()  # Sort the array to facilitate the two-pointer technique
        n = len(nums)  # Get the length of the list
        
        for i in range(n):
            # If the current value is the same as the one before, skip it to avoid duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j, k = i + 1, n - 1  # Initialize two pointers
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]  # Calculate the sum of the triplet
                
                if total < 0:  # If the sum is less than 0, move the left pointer to the right
                    j += 1
                elif total > 0:  # If the sum is greater than 0, move the right pointer to the left
                    k -= 1
                else:
                    # If the sum is 0, add the triplet to the result
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    
                    # Skip duplicates for the second number
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                        
                    # Skip duplicates for the third number
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        
        return res  # Return the list of triplets

# Example usage:
nums = [-1, 0, 1, 2, -1, -4]
sol = Solution()
print(sol.threeSum(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]
