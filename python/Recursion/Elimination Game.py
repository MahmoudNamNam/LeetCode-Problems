class Solution:
    def lastRemaining(self, n: int) -> int:
        def helper(n, left_to_right):
            if n == 1:
                return 1
            if left_to_right or n % 2 :
                return 2 * helper(n // 2, not left_to_right)
            else:
                return 2 * helper(n // 2, not left_to_right) - 1
        
        return helper(n, True)
