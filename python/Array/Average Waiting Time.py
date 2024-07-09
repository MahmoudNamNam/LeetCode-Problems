from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current_time  = 0  # Keeps track of when the chef will be available to take the next order
        total_waiting_time  = 0  # Accumulates the total waiting time for all customers

        # Iterate over each customer in the list
        for arrival, prep_time  in customers:
            # The chef starts preparing the order either when the chef is available or when the customer arrives, whichever is later
            current_time  = max(current_time , arrival) + prep_time 
            # Calculate the waiting time for the current customer and add it to total_waiting_time 
            total_waiting_time  += current_time  - arrival
        
        # Calculate the average waiting time by dividing the total waiting time by the number of customers
        return total_waiting_time  / len(customers)

# Example usage
solution = Solution()

customers1 = [[1, 2], [2, 5], [4, 3]]
print(f"Average waiting time for customers1: {solution.averageWaitingTime(customers1):.5f}")

customers2 = [[5, 2], [5, 4], [10, 3], [20, 1]]
print(f"Average waiting time for customers2: {solution.averageWaitingTime(customers2):.5f}")
