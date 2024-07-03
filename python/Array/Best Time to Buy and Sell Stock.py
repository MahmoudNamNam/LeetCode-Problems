from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the minimum price to a very large value
        min_price = float('inf')
        # Initialize the maximum profit to 0
        max_profit = 0
        
        # Iterate through each price in the list
        for price in prices:
            # Update the minimum price if the current price is lower
            if price < min_price:
                min_price = price
            # Calculate the profit if we sold at the current price
            profit = price - min_price
            # Update the maximum profit if the current profit is higher
            if profit > max_profit:
                max_profit = profit
        
        # Return the maximum profit found
        return max_profit

# Example usage:
solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5
print(solution.maxProfit([7, 6, 4, 3, 1]))     # Output: 0
