class Solution:
    def divide_array(self, nums, k):
        # Sort the input array
        nums.sort()
        ans = []

        # Iterate through the sorted array in steps of 3
        for i in range(0, len(nums)-2, 3):
            # Check if the difference between the last and first element in the current subarray is greater than k
            if nums[i+2] - nums[i] > k:
                return []  # Return an empty list if conditions cannot be satisfied
            
            # Add the current subarray to the result
            ans.append([nums[i], nums[i+1], nums[i+2]])

        return ans

# Example usage:
solution = Solution()

# Example 1
nums1 = [1, 3, 4, 8, 7, 9, 3, 5, 1]
k1 = 2
output1 = solution.divide_array(nums1, k1)
print(output1)

# Example 2
nums2 = [1, 3, 3, 2, 7, 3]
k2 = 3
output2 = solution.divide_array(nums2, k2)
print(output2)
