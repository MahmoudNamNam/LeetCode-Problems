'''
solution #1
For n > 1, Fn should return Fn-1 + Fn-2.
Time complexity : 2 ^n
'''

class Solution:
    def fib(self, n: int) -> int:
        if(n<2):
            return n
        else:
            return self.fib(n-1)+self.fib(n-2)


'''
Solution #2
we are computing the already computed values of fib. Since there are overlapping subproblems, we can create and store the fib values in an array.
    Complexity
    Time complexity: O(n) (Linear complexity)
    Space complexity: O(n) since we store the fib values in array.
'''


class Solution:
    def fib(self, n: int) -> int:
        if(n==0):
            return 0
        dp = [-1]*(n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


'''
Solution #3; O(1) solution using Math
When we take any two successive (one after the other) Fibonacci Numbers, their ratio is very close to the Golden Ratio "φ" which is approximately 1.618034...
'''


class Solution:
    def fib(self, n: int) -> int:
        golden_ratio = (1 + 5 ** 0.5) / 2
        return int((golden_ratio ** n + 1) / 5 ** 0.5)




# Memo
class Solution:
    def __init__(self):
        self.dp = {}

    def fib(self, n):
        if n <= 1:
            return n
        if n in self.dp:
            return self.dp[n]
        self.dp[n] = self.fib(n-1) + self.fib(n-2)
        return self.dp[n]
sol = Solution()
print(sol.fib(10))  