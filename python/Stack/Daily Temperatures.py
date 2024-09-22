from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Get the length of the input array
        n = len(temperatures)
        # Initialize the answer array with zeros
        answer = [0] * n
        # Stack to keep track of indices of temperatures
        stack = []

        # Iterate through each day
        for i in range(n):
            # Check if the stack is not empty and the current temperature is greater
            # than the temperature at the index on top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # If condition is true, update answer for the previous day
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
                # print(f"the previndex: {prev_index}")
                # print(f"answer[prev_index]: {answer[prev_index]}")

            # Push the current index onto the stack for future comparisons
            stack.append(i)

        # Return the final answer array
        return answer

# Example usage:
solution = Solution()

# Example 1
temperatures1 = [73,74,75,71,69,72,76,73]
output1 = solution.dailyTemperatures(temperatures1)
print(output1)  # Output: [1,1,4,2,1,1,0,0]

# # Example 2
# temperatures2 = [30,40,50,60]
# output2 = solution.dailyTemperatures(temperatures2)
# print(output2)  # Output: [1,1,1,0]

# # Example 3
# temperatures3 = [30,60,90]
# output3 = solution.dailyTemperatures(temperatures3)
# print(output3)  # Output: [1,1,0]



"""
	 * Reverse thinking
	 * 	Instead of finding the next greater of an element
	 * 	Use an element to find all items it is greater than them
	 *
	 * We will add each new element in the stack waiting for its next greater
	 *
	 * Given a new number, iterate on all previous in the stack
	 * 	and mark my self as their next great
	 * 	but stop once found a number >= me
	 * 	why? because I can't be used for more numbers (he is better than me)
	 *
	 * 	Example: {30, 20, 10, 7, 8, 15}
	 * 	Assume stack has now positions for { 30, 20, 10, 7}
	 * 	Now we have 8: 8 pops from stack 7 as it is > than it, but stop at 10
	 * 	Now we have 15: 15 pops from stack 8, 10 as it is > than it, but stop at 20
	 * 	and so on
	 *
	 * O(n) time! We iterate on numbers ~twice
"""
