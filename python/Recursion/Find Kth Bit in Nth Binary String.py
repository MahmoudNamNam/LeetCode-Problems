class Solution:
    def findS_i(self, n):
        if n == 1:
            return '0'
        prev = self.findS_i(n - 1)
        return prev + '1' + ''.join('1' if bit == '0' else '0' for bit in reversed(prev))

    def findKthBit(self, n: int, k: int) -> str:
        s = self.findS_i(n)
        return s[k - 1]  


sol = Solution()

print(sol.findS_i(4))