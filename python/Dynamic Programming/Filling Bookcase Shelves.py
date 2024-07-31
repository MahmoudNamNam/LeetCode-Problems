from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        
        # DP array to store the minimum height to place the first i books
        dp = [0] + [float('inf')] * n
        
        for i in range(1, n + 1):
            width = 0   # Current shelf width
            height = 0  # Maximum height of the current shelf
            
            # Iterate backwards to consider placing the current book on a new shelf
            for j in range(i - 1, -1, -1):
                width += books[j][0]  # Accumulate the width of books from j to i-1
                
                # If accumulated width exceeds shelf width, we cannot place more books on this shelf
                if width > shelfWidth:
                    break
                
                # Update the height of the current shelf
                height = max(height, books[j][1])
                
                # Update the dp array with the minimum height by considering placing books from j to i-1 on the same shelf
                dp[i] = min(dp[i], dp[j] + height)
        
        # The last element of the dp array will have the minimum possible height for placing all books
        return dp[n]


sol =Solution()
print(sol.minHeightShelves([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4))  # Output: 6
print(sol.minHeightShelves([[1,3],[2,4],[3,2]], 6))  # Output: 4