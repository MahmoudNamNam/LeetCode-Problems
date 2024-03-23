from typing import List

class Solution:
    """
    This class implements the maxArea function which calculates the maximum area of water that can be trapped between two buildings.
    """

    def maxArea(self, height: List[int]) -> int:
        """
        This function calculates the maximum area of water that can be trapped between two buildings.

        :param height: A list of integers representing the heights of buildings.
        :return: An integer representing the maximum area of water that can be trapped.
        """
        maxArea = 0  # Initialize the maximum area to 0
        left = 0     # Initialize the left pointer
        right = len(height) - 1  # Initialize the right pointer

        # Continue the while loop until the left pointer is less than the right pointer
        while left < right:
            width = right - left  # Calculate the width between the two pointers
            min_height = min(height[left], height[right])  # Find the minimum height between the two buildings
            area = min_height * width  # Calculate the area with the current width and minimum height
            maxArea = max(maxArea, area)  # Update the maximum area if the current area is larger

            # Move the left pointer if the height of the left building is less than the height of the right building
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea  # Return the maximum area after the while loop

# Example usage:
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution().maxArea(height))  # Print the maximum area for the given building heights