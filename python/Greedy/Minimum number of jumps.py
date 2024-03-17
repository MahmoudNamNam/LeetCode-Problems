class Solution:
    def minJumps(self, arr):
        """
        Calculates the minimum number of jumps required to reach the end of the array.

        Parameters:
        arr (List[int]): A list of non-negative integers representing the maximum jump length at each position.
        n (int): The length of the input array.

        Returns:
        int: The minimum number of jumps required to reach the end of the array. Returns -1 if it's not possible to reach the end.

        Example:
        >>> solution = Solution()
        >>> solution.minJumps([2, 3, 1, 1, 4], 5)
        2
        >>> solution.minJumps([3, 2, 1, 0, 4], 5)
        -1
        """
        if len(arr) <= 1:  # If the array has only one element or is empty, no jumps are needed
            return 0
        
        if arr[0] == 0:  # If the first element is 0, we can't move forward
            return -1
        
        max_reachable = arr[0]  # Initialize the maximum reachable index from the current position
        steps = arr[0]  # Initialize the steps left at the current position
        jumps = 1  # Initialize the number of jumps
        
        for i in range(1, len(arr)):  # Iterate through the array starting from the second element
            if i == len(arr) - 1:  # If we reach the last element, return the number of jumps
                return jumps
            
            max_reachable = max(max_reachable, i + arr[i])  # Update the maximum reachable index
            
            steps -= 1  # Decrement the steps left
            
            if steps == 0:  # If no steps left, we must jump to the next max reachable index
                jumps += 1
                
                if i >= max_reachable:  # If the current index is not reachable anymore, return -1
                    return -1
                
                steps = max_reachable - i  # Update steps to the difference between max_reachable and current index
    
        return -1  # If we can't reach the end of the array


s = Solution()

c= s.minJumps([2, 3, 1, 2, 4, 2, 1, 0, 3])
print("Number of minimum jumps required : ",c)