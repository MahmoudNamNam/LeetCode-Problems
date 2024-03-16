class Solution(object):
    def canJump(self, arr):
        """
        Determines whether it's possible to reach the last index of the array from the first index.

        Parameters:
        arr (List[int]): A list of non-negative integers representing the maximum jump length at each position.

        Returns:
        bool: True if it's possible to reach the last index, False otherwise.
        
        Example:
        >>> solution = Solution()
        >>> solution.canJump([2, 3, 1, 1, 4])
        True
        >>> solution.canJump([3, 2, 1, 0, 4])
        False
        """
        max_reachable = 0  # Initialize the maximum reachable index
        n = len(arr)
        
        for i in range(n):  # Iterate through the array
            if i > max_reachable:  # If the current index is not reachable, return False
                return False
            max_reachable = max(max_reachable, i + arr[i])  # Update the maximum reachable index
        
        return True  # If we reach here, it means we can reach the end of the array
