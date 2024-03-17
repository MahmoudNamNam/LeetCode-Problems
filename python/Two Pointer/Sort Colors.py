class Solution:
    def sort012(self, arr, n):
        """
        Sorts an array containing 0s, 1s, and 2s in ascending order.
        
        Parameters:
        - arr (list): The input array containing 0s, 1s, and 2s.
        - n (int): The number of elements in the array.
        
        Returns:
        - list: The sorted array.
        
        Dutch National Flag algorithm is used to solve this problem efficiently 
        in O(n) time complexity. It sorts the array by partitioning it into three 
        sections - 0s, 1s, and 2s, and moving elements to their correct positions.
        
        Example:
        >>> solution = Solution()
        >>> arr = [2, 1, 0, 1, 2, 0, 1]
        >>> sorted_arr = solution.sort012(arr, len(arr))
        >>> sorted_arr
        [0, 0, 1, 1, 1, 2, 2]
        """
        low = 0
        high = n - 1
        mid = 0

        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

        return arr



solution = Solution()
arr = [2, 1, 0, 1, 2, 0, 1]
sorted_arr = solution.sort012(arr, len(arr))