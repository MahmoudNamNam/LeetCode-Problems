from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n=len(skill)
        if n == 2:
            return skill[0]*skill[1]
        skill.sort()
        target = skill[0] + skill[-1]
        l=0
        r=n-1
        res=0
        while l < r:
            if skill[l] + skill[r] != target:
                return -1 
            res += skill[l] * skill[r]
            l += 1
            r -= 1
        return res
    
sol = Solution()

print(sol.dividePlayers([3,2,5,1,3,4]))
print(sol.dividePlayers([3,4]))
print(sol.dividePlayers([1,1,2,3]))