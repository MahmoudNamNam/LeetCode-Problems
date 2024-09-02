from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        i=0
        while True:
            idx = i%n
            if chalk[idx] <= k:
                k -= chalk[idx]
                i+=1
            else:
                return idx

sol = Solution()

chalk = [5,1,5]
k = 22

print(sol.chalkReplacer(chalk,k))


chalk = [3,4,1,2]
k = 25
print(sol.chalkReplacer(chalk,k))