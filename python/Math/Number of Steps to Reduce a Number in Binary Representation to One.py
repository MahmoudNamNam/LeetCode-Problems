class Solution:
    def binaryToDecimal(self,n):
        return int(n,2)
    def numSteps(self, s: str) -> int:
        num= self.binaryToDecimal(s)
        res=0
        while num !=1:
            res+=1
            if num %2:
                num+=1
            else:
                num //= 2
        return res


sol = Solution()

print(sol.numSteps(s = "1101"))
print(sol.numSteps(s = "10"))
print(sol.numSteps(s = "1"))