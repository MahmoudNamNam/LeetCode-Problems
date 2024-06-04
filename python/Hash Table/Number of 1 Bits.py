from collections import Counter



class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = Counter(bin(n))
        return counter['1']

sol=Solution()
print(sol.hammingWeight(2147483645))