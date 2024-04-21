class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)  
        nums[:] = nums[-k:] + nums[:-k]  # Update the elements of nums in-place

s = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

print("Before rotation:", nums)
s.rotate(nums, k)
print("After rotation:", nums)  # [5, 6, 7, 1, 2, 3, 4]
