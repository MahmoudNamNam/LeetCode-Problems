from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        
        # Step 1: Calculate the total sum required
        total_sum = mean * (n + m)
        
        # Step 2: Calculate the sum of known rolls
        known_sum = sum(rolls)
        
        # Step 3: Calculate the sum of the missing rolls
        missing_sum = total_sum - known_sum
        
        # Step 4: Check if the missing_sum is achievable
        if missing_sum < n or missing_sum > 6 * n:
            return []
        
        # Step 5: Distribute the missing_sum among the n missing rolls
        # Start by giving each missing roll the minimum possible value of 1
        result = [1] * n
        missing_sum -= n  # Subtract the n "1"s we just distributed
        
        # Distribute the remaining missing_sum over the n rolls
        i = 0
        while missing_sum > 0:
            add = min(missing_sum, 5)  # We can add at most 5 to each roll to keep it in the range [1,6]
            result[i] += add
            missing_sum -= add
            i += 1
        
        return result

sol =Solution()
print(sol.missingRolls(rolls = [3,2,4,3], mean = 4, n = 2))
print(sol.missingRolls(rolls = [1,5,6], mean = 3, n = 4))
print(sol.missingRolls(rolls = [1,2,3,4], mean = 6, n = 4))