from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l= 0
        r = len(height)-1
        lMax=height[0]
        rMax=height[r]
        sm=0
        while (l < r):
            if lMax <= rMax:
                sm +=  lMax - height[l]
                l+=1
                lMax=max(lMax,height[l])
            else:
                sm +=  rMax - height[r]
                r-=1
                rMax=max(rMax,height[r])
        return sm

s= Solution()
s.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1])