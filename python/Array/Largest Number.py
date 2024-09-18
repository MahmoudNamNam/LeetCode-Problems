from functools import cmp_to_key
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert the list of numbers to strings
        nums = list(map(str, nums))
        
        # Define a comparator that compares two strings based on concatenated order
        def compare(a, b): 
            if a + b > b + a:  #* If a + b > b + a, then a should come before b in the final result.
                return -1  # a should come before b
            elif a + b < b + a:
                return 1   # b should come before a
            else:
                return 0   # they are equal in terms of order
        
        # Sort the numbers based on the custom comparator
        nums.sort(key=cmp_to_key(compare))
        
        # Join the numbers to form the largest number
        largest_num = ''.join(nums)
        
        # Edge case: if the largest number starts with '0', that means all numbers were '0'
        if largest_num[0] == '0':
            return '0'
        
        return largest_num

sol = Solution()
print(sol.largestNumber([10, 2]))       # Output: "210"
