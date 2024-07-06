class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # The cycle length is 2 * (n - 1) because the pillow goes to the end and then back to the start
        cycle_length = 2 * (n - 1)
        
        # Find the effective time within one cycle
        time %= cycle_length
        
        # Determine the position based on the effective time
        if time < n:
            # Moving forward
            return time + 1
        else:
            # Moving backward
            return 2 * n - time - 1

# Example 1
n = 4
time = 5
solution = Solution()
print(solution.passThePillow(n, time))  # Output: 2

# Example 2
n = 3
time = 2
print(solution.passThePillow(n, time))  # Output: 3
