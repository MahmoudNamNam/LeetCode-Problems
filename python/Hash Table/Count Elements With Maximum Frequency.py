from typing import List
from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Step 1: Count the frequency of each element in 'nums' list.
        freq_counter = Counter(nums)
        
        # Initialize variables to store the maximum number of elements with same frequency and the current





#* Input: nums = [1,2,2,3,1,4]
#* Output: 4



from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums):
        # Create a Counter object to count the frequency of elements
        counts = Counter(nums)
        
        # Find the maximum frequency
        max_frequency = max(counts.values())
        
        # Count the elements with maximum frequency
        max_frequency_elements_count =0
        for k, v in counts.items():
            if v == max_frequency:
                max_frequency_elements_count += 1
        
        # Return the result
        return max_frequency * max_frequency_elements_count
nums = [1,2,2,3,1,4]        
counts = Counter(nums)
        # Find the maximum frequency
max_frequency = max(counts.values())
print(max_frequency)
sol=Solution()
print(sol.maxFrequencyElements(nums))