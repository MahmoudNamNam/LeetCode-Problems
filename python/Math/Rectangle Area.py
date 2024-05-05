class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        a1=(ax2-ax1)*(ay2-ay1)
        a2=(bx2-bx1)*(by2-by1)
        x1=max(ax1,bx1)
        x2=min(ax2,bx2)
        y1=max(ay1,by1)
        y2=min(ay2,by2)
        if x2-x1<0 or y2-y1<0: 
            return a1+a2
        a3=(x2-x1)*(y2-y1)
        return a1+a2-a3
    
    def computeArea_(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        A1=(ax2-ax1)*(ay2-ay1)
        A2=(bx2-bx1)*(by2-by1)
        if ax2<=bx1 or ay1>=by2 or ax1>=bx2 or ay2<=by1:
            return A1+A2
        length=min(ax2,bx2)-max(ax1,bx1)
        height=min(ay2,by2)-max(ay1,by1)
        overlap_area=length*height
        return A1+A2-overlap_area


s = Solution()
# Rectangles:
# Rectangle A: (-3, 0) to (3, 4)
# Rectangle B: (0, -1) to (9, 2)
sol =  s.computeArea(ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2)
print(sol)

