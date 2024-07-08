
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ans=0
        for i in range(1,n+1):
            ans =(ans +k)%i
        return ans +1


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Create a list to represent friends
        friends = list(range(1, n + 1))
        
        # Initialize the starting index
        index = 0
        
        # Continue until only one friend remains
        while len(friends) > 1:
            # Find the index of the friend to eliminate
            index = (index + k - 1) % len(friends)
            # Remove the friend from the circle
            friends.pop(index)
        
        # The remaining friend is the winner
        return friends[0]

# Example usage and debug
solution = Solution()

# Example 1
n = 5
k = 2
print(f"Winner for n={n}, k={k}: {solution.findTheWinner(n, k)}")  # Expected output: 3

# Example 2
n = 6
k = 5
print(f"Winner for n={n}, k={k}: {solution.findTheWinner(n, k)}")  # Expected output: 1
