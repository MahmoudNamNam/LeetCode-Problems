from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k ==1:
            return nums
        n = len(nums)
        res = [-1] * (n - k + 1)
        seq =1 # Track the length of the current consecutive sequence
        for i in range(n-1):
            if nums[i] +1 == nums[i+1]: # Check for Cons ELE 
                seq +=1
            else:
                seq = 1
            
            if seq >= k:
                res[i - k + 2] = nums[i + 1]

        
        return res


sol =Solution()
print(sol.resultsArray(nums = [1,2,3,4,3,2,5], k = 3))
print(sol.resultsArray(nums = [2,2,2,2,2], k = 4))
print(sol.resultsArray(nums = [3,2,3,2,3,2], k = 2))