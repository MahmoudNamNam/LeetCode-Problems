from typing import List


nums = [0,0,1,1,1,2,2,3,3,4]

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k


sol=Solution()
k =sol.removeDuplicates(nums)
print(sol.removeDuplicates(nums))

for i in range(k):
    print(nums[i],end=' ')