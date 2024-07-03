from typing import List



class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # If the array has 4 or fewer elements, we can change all of them to be the same in at most 3 moves.
        if len(nums) <= 4:
            return 0
        
        # Sort the array to easily access the smallest and largest elements.
        nums.sort()
        
        # Considering the possible scenarios:
        # 1. Change the 3 largest elements to the 4th largest element.
        # 2. Change the 2 largest elements to the 3rd largest element and the smallest element to the 2nd smallest element.
        # 3. Change the largest element to the 2nd largest element and the two smallest elements to the 2nd smallest element.
        # 4. Change the 3 smallest elements to the smallest element.
        
        return min(nums[-1] - nums[3],  # Change the 3 smallest elements
                   nums[-2] - nums[2],  # Change the smallest element and the two largest elements
                   nums[-3] - nums[1],  # Change the two smallest elements and the largest element
                   nums[-4] - nums[0])  # Change the 3 largest elements

sol =Solution()

print(sol.minDifference([5,3,2,4]))
print(sol.minDifference([1,5,0,10,14]))