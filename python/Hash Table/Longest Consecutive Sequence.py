from typing import Counter, List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        counter = Counter(nums)
        res=1
        keys= sorted(list(counter.keys()))
        curr_len=1
        for i in range(1,len(keys)):
            if keys[i]-keys[i-1] ==1:
                curr_len+=1
            else :
                curr_len=1
            res=max(curr_len,res)
            
        
        return res

sol = Solution()
print(sol.longestConsecutive(nums = [100,4,200,1,3,2])) #4
print(sol.longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1])) # 9