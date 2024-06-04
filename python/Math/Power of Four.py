import numpy as np

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        log_result = np.emath.logn(4, n)
        return log_result == int(log_result)

sol = Solution()
print(sol.isPowerOfFour(16))  # True
print(sol.isPowerOfFour(15))  # False
print(sol.isPowerOfFour(1))   # True
print(sol.isPowerOfFour(64))  # False


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        if n == 1:
            return True
        return self.isPowerOfFour(n / 4)
        