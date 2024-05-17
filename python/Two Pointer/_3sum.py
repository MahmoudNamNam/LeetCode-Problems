from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j, k = i + 1, n - 1
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                        
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        
        return res


nums = [-1,0,1,2,-1,-4]

sol = Solution()

sol.threeSum(nums)