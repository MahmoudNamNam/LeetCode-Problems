class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Initialize two variables to store the smallest and second smallest elements encountered so far
        first = second = float('inf') 
        
        # Iterate through each element in the input list
        for n in nums: 
            # If the current element is less than or equal to the smallest element encountered so far,
            # update the smallest element to the current element
            if n <= first: 
                first = n
            # If the current element is greater than the smallest element but less than or equal to
            # the second smallest element encountered so far, update the second smallest element to the current element
            elif n <= second:
                second = n
            # If the current element is greater than both the smallest and second smallest elements encountered so far,
            # it means we've found an increasing triplet, so return True
            else:
                return True
        
        # If the loop completes without finding an increasing triplet, return False
        return False
