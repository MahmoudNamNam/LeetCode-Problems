# Solution 1: Iterative Approach

class Solution:
    def addDigits(self, num: int) -> int:
        numStr = str(num)
        while len(numStr)!=1:
            res=0
            for i in numStr:
                res += int(i)
            numStr = str(res)
        return int(numStr)

sol = Solution()

print(sol.addDigits(381))

# Mathematical Approach (Digital Root)
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9