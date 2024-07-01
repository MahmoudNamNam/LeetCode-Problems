from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n  # Initialize the answer array with 0s
        stack = []  # Stack to keep track of the indices of the temperatures
        
        for i in range(n):
            # Check if the current temperature is higher than the temperature at the index at the top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()  # Get the index of the day from the stack
                answer[idx] = i - idx  # Calculate the number of days to wait for a warmer temperature
            stack.append(i)  # Push the current index onto the stack
        
        return answer
    
sol = Solution()
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))