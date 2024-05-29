from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        content = 0
        lenS=len(s)
        lenG=len(g)
        if lenS == 0 :
            return content
        g.sort()
        s.sort()
        j=i=0
        while j<lenS and i < lenG:
            if s[j]>=g[i]:
                content += 1
                i+=1
                j+=1
            else:
                j+=1
        return content
    
    
    
sol = Solution()
print(sol.findContentChildren(g = [1,2,3], s = [1,1]))
print(sol.findContentChildren(g = [1,2], s = [1,2,3]))