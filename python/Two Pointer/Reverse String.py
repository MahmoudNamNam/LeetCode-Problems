# two pointer

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        l,r=0,len(s)-1
        while l<r:
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
        return s
        """
        Do not return anything, modify s in-place instead.
        """

sol = Solution()
s = ["H","a","n","n","a","h"]
sol.reverseString(s)
print(s)