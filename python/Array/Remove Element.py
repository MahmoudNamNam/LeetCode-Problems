from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Approach:
        # Use list comprehension to create a new list with elements not equal to `val`
        # Replace the original list `nums` with this new list
        # Return the length of the updated list
        
        # Time complexity: O(n) - We iterate through the list once
        # Space complexity: O(n) - We create a new list that could be as large as the input list
        nums[:] = [x for x in nums if x != val]
        return len(nums)
        
nums = [3,2,2,3]
val = 3

sol = Solution()
sol.removeElement(nums,val)

print(nums)  # Output: [2, 2]





class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Approach:
        # Use two pointers: `left` and `right`
        # `right` iterates through the list
        # `left` tracks the position to copy elements not equal to `val`
        # Modify the list in place and return the new length
        
        # Time complexity: O(n) - Each element is checked once
        # Space complexity: O(1) - No additional space proportional to the input size is used
        left, right = 0, 0

        while right < len(nums):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
            right += 1

        return left

nums = [3,2,2,3]
val = 3

sol = Solution()
sol.removeElement(nums,val)

print(nums[:sol.removeElement(nums, val)])  # Output: [2, 2]




'''Third Sol'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Approach:
        # Use a while loop to repeatedly remove elements equal to `val`
        # Continue until no elements equal to `val` are left
        # Return the length of the updated list
        
        # Time complexity: O(n^2) in the worst case - `remove()` is O(n) and could be called up to `n` times
        # Space complexity: O(1) - Modifies the list in place without additional space proportional to input size
        while val in nums:
            nums.remove(val)
        return len(nums)

nums = [3,2,2,3]
val = 3

sol = Solution()
sol.removeElement(nums,val)

print(nums)  # Output: [2, 2]
