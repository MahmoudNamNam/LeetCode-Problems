class Solution(object):
    def maxSubArray(self, nums):
        """
        Finds the maximum sum of a contiguous subarray within the given array.

        Parameters:
        nums (List[int]): A list of integers representing the input array.

        Returns:
        int: The maximum sum of a contiguous subarray within the given array.

        Example:
        >>> solution = Solution()
        >>> solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6
        """
        currentMax = nums[0]  # Initialize current maximum sum with the first element
        overallMax = nums[0]  # Initialize overall maximum sum with the first element

        # Iterate over the array starting from the second element
        for num in nums[1:]:
            # Determine the maximum sum ending at the current element
            currentMax = max(num, currentMax + num)
            # Update the overall maximum sum if needed
            overallMax = max(overallMax, currentMax)

        return overallMax


# * Second Sol
    

class Solution(object):
    def maxSubArray(self, nums):
        """
        Finds the maximum sum of a contiguous subarray within the given array.

        Parameters:
        nums (List[int]): The array of integers.

        Returns:
        int: The maximum sum of a contiguous subarray within the given array.
        
        Example:
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        Output: 6
        Explanation: [4,-1,2,1] has the largest sum = 6.
        """
        a = nums[0]  # Initialize the maximum sum to the first element of nums
        sum = 0  # Initialize the current sum to 0
        for i in nums:
            if sum < 0:
                sum = 0  # If the current sum becomes negative, reset it to 0
            sum += i  # Add the current element to the current sum

            if sum > a:
                a = sum  # Update the maximum sum if the current sum is greater

        return a

solution = Solution()
print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))