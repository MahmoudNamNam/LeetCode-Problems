from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()  
        start = 0
        max_beauty = 0

        for end in range(len(nums)):
            while nums[end] - nums[start] > 2 * k:
                start += 1 

            max_beauty = max(max_beauty, end - start + 1)

        return max_beauty
    

sol = Solution()
print(sol.maximumBeauty(nums = [4,6,1,2], k = 2))
print(sol.maximumBeauty(nums = [1,1,1,1], k = 10))