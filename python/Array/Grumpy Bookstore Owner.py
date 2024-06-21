from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        total_satisfied = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                total_satisfied += customers[i]
        
        max_additional_satisfaction = 0
        current_additional_satisfaction = 0
        
        for i in range(minutes):
            if grumpy[i] == 1:
                current_additional_satisfaction += customers[i]
        
        max_additional_satisfaction = current_additional_satisfaction
        
        for i in range(minutes, len(customers)):
            if grumpy[i] == 1:
                current_additional_satisfaction += customers[i]
            if grumpy[i - minutes] == 1:
                current_additional_satisfaction -= customers[i - minutes]
            
            max_additional_satisfaction = max(max_additional_satisfaction, current_additional_satisfaction)
        
        return total_satisfied + max_additional_satisfaction



sol = Solution()
customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3
print(sol.maxSatisfied(customers,grumpy,minutes)) # Output: 16

'''
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
'''