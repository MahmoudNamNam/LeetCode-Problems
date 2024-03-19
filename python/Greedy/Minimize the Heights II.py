class Solution:
    def getMinDiff(self, arr, n, k):
        """
        Calculates the minimum difference between the heights of the towers after adjusting them by at most k units.

        Parameters:
        - arr (list of int): An array representing the heights of the towers.
        - n (int): The number of towers.
        - k (int): The maximum number of units by which a tower's height can be adjusted.

        Returns:
        - int: The minimum difference between the heights of the towers after adjustments.

        Example:
        solution = Solution()
        towers = [1, 5, 8, 10]
        k = 2
        n = len(towers)
        min_diff = solution.getMinDiff(towers, n, k)
        # Output: 5 (Adjusting the first tower to height 3 and the last tower to height 6 results in a minimum difference of 5)
        """
        arr.sort()
        ans = arr[n - 1] - arr[0]  # Initialize ans with the maximum possible difference
        for i in range(n - 1):
            mn = min(arr[0] + k, arr[i + 1] - k)
            mx = max(arr[-1] - k, arr[i] + k)
            if mn >= 0:  # Ensure mn is not negative
                ans = min(ans, mx - mn)
        return ans
