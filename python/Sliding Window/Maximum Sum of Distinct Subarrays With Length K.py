from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n < k:
            return 0

        max_sum = 0
        current_sum = 0
        start = 0
        elements = set()

        for end in range(n):
            while nums[end] in elements:
                elements.remove(nums[start])
                current_sum -= nums[start]
                start += 1

            elements.add(nums[end])
            current_sum += nums[end]

            if end - start + 1 == k:
                max_sum = max(max_sum, current_sum)
                elements.remove(nums[start])
                current_sum -= nums[start]
                start += 1

        return max_sum


'https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/solutions/5364323/solution-with-99-94-beats/'

nums1 = [1, 5, 4, 2, 9, 9, 9]
k1 = 3
print(Solution().maximumSubarraySum(nums1, k1))  # Output: 15

nums2 = [4, 4, 4]
k2 = 3
print(Solution().maximumSubarraySum(nums2, k2))  # Output: 0