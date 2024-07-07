class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # Initialize total number of bottles drunk to the initial number of bottles
        total_drunk = numBottles
        
        # Continue the process as long as we have enough bottles to exchange for at least one full bottle
        while numBottles >= numExchange:
            # Calculate the number of new bottles we can get by exchanging
            new_bottles = numBottles // numExchange
            # Update the total number of bottles drunk
            total_drunk += new_bottles
            # Update numBottles to the new number of full bottles plus the remainder empty bottles
            numBottles = new_bottles + (numBottles % numExchange)
        
        # Return the total number of bottles drunk
        return total_drunk

sol = Solution()
print(sol.numWaterBottles(numBottles=9, numExchange=3))  # Output: 13
print(sol.numWaterBottles(numBottles=15, numExchange=4)) # Output: 19
