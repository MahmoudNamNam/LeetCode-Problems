from collections import Counter

class Solution:
    def frequencySort(self, nums):
        cnt = Counter(nums)
        # Sort first by frequency (ascending) and then by value (descending)
        sorted_nums = sorted(nums, key=lambda x: (cnt[x], -x))
        return sorted_nums

# Test examples
solution = Solution()
print(solution.frequencySort([1, 1, 2, 2, 2, 3])) # Output: [3, 1, 1, 2, 2, 2]
print(solution.frequencySort([2, 3, 1, 3, 2]))   # Output: [1, 3, 3, 2, 2]
print(solution.frequencySort([-1, 1, -6, 4, 5, -6, 1, 4, 1])) # Output: [5, -1, 4, 4, -6, -6, 1, 1, 1]

""""
sorted(nums, key=lambda x: (cnt[x], -x)):
The key function sorts by the frequency cnt[x] in ascending order.
If two elements have the same frequency, it then sorts by the element value -x in descending order.

"""