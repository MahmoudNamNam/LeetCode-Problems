class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        
        output = ""
        
        while n != 0:
            # Append the least significant bit of n to the output string
            output = str(n & 1) + output
            
            # Update n for the next iteration by dividing by -2 (negating after right shift)
            n = -(n >> 1)
        return output

sol = Solution()
print(sol.baseNeg2(2))  # 110
print(sol.baseNeg2(3))  # 111
print(sol.baseNeg2(4))  # 100