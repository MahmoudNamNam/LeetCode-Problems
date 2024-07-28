from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert integers to strings for comparison
        nums_str = list(map(str, nums))
        # Sort the array with a custom comparator
        nums_str.sort(key=lambda x: x*10, reverse=True)
        # Join sorted numbers into a single string
        largest_num = ''.join(nums_str)
        # Strip leading zeros
        return '0' if largest_num[0] == '0' else largest_num

# Examples
sol = Solution()
print(sol.largestNumber([10, 2]))       # Output: "210"
