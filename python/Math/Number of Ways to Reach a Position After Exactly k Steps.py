class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
            MOD = 10**9 + 7

            # Calculate the necessary moves
            delta = abs(endPos - startPos)
            
            # If the required moves are greater than k or the parity doesn't match, return 0
            if delta > k or (k - delta) % 2 != 0:
                return 0
            
            # Calculate r
            r = (k + delta) // 2
            
            # Calculate the binomial coefficient C(k, r)
            def binomial_coefficient(n, k):
                if k > n:
                    return 0
                if k == 0 or k == n:
                    return 1
                k = min(k, n - k)
                c = 1
                for i in range(k):
                    c = c * (n - i) // (i + 1)
                return c
            
            return binomial_coefficient(k, r) % MOD



sol = Solution()

print(sol.numberOfWays(1, 2, 3))
print(sol.numberOfWays(2, 5, 10))