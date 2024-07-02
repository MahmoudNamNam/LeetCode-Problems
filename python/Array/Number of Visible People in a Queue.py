from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        answer = [0] * n  # Initialize the answer array with 0s
        stack = []  # Stack to keep track of indices

        # Traverse the heights array from right to left
        for i in range(n - 1, -1, -1):
            # Count how many people can be seen
            while stack and heights[i] > heights[stack[-1]]:
                stack.pop()
                answer[i] += 1
            
            # If stack is not empty, the current person can see the next taller person
            if stack:
                answer[i] += 1
            
            # Push the current index onto the stack
            stack.append(i)
        
        return answer

sol = Solution()
print(sol.canSeePersonsCount([10, 6, 8, 5, 11, 9]))  # Output: [3, 1, 2, 1, 1, 0]
print(sol.canSeePersonsCount([5, 1, 2, 3, 10]))      # Output: [4, 1, 1, 1, 0]