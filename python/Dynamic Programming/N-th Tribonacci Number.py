class Solution:
    def __init__(self):
        self.memo = {}

    def tribonacci(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        result = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        self.memo[n] = result
        return result
