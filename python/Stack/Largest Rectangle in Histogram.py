from typing import List




class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack =  []
        res=0
        n= len(heights)
        for i in range(n):
            idx = i
            while stack and stack[-1][0] > heights[i]:
                val ,idx = stack.pop()
                res =max(res,val *(i-idx))
            stack.append([heights[i],idx])
        for i in stack:
            res = max(res,(n-i[1])*i[0])
        return res




class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  
        max_area = 0
        heights.append(0)  # Add a sentinel value to flush out remaining bars in the stack

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]  
                width = i if not stack else i - stack[-1] - 1  
                max_area = max(max_area, height * width)
            stack.append(i)
        
        return max_area