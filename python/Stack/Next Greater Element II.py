from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n 
        stack = []
        
        for i in range(2 * n):
            num = nums[i % n] 
            while stack and nums[stack[-1]] < num:
                index = stack.pop()
                result[index] = num
            if i < n:
                stack.append(i)
        
        return result



sol = Solution()
print(sol.nextGreaterElements([1,2,1]))




class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n  
        stack = []  
        
        for i in range(2 * n):
            index = i % n  
            while stack and nums[stack[-1]] < nums[index]:
                result[stack.pop()] = nums[index]
            if i < n:
                stack.append(i)
        
        return result