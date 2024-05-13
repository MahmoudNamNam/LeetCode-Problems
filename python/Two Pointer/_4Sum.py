from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        s = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                l = j+1
                r = len(nums)-1
                while l<r:
                    if nums[i] + nums[j] + nums[l] + nums[r]<target:
                        l+=1
                    elif nums[i] + nums[j] + nums[l] + nums[r]>target:
                        r-=1
                    elif nums[i] + nums[j] + nums[l] + nums[r]==target:
                        s.add((nums[i],nums[j],nums[l],nums[r]))
                        l+=1
                        r-=1
        return list(s)

# -------------------------------------------------------------------------




class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate i
                continue
            
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:  # Skip duplicate j
                    continue
                
                l = j + 1
                r = n - 1
                
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    
                    if total < target:
                        l += 1
                    elif total > target:
                        r -= 1
                    else:
                        result.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        
                        while l < r and nums[l] == nums[l - 1]:  # Skip duplicate l
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:  # Skip duplicate r
                            r -= 1
        
        return result


s = Solution()
print(s.fourSum(nums = [1,0,-1,0,-2,2], target = 0))



