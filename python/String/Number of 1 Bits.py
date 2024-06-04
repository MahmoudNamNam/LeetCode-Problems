class Solution:
    def hammingWeight(self, n: int) -> int:
        b = format(n, 'b')
        return b.count("1")
sol=Solution()
print(sol.hammingWeight(2147483645))