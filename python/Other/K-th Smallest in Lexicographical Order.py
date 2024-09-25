from typing import List

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def countSteps(n, curr):
            steps = 0
            first = curr
            last = curr
            while first <= n:
                steps += min(last, n) - first + 1
                first *= 10
                last = last * 10 + 9
            return steps
        
        num = 1
        k -= 1  
        
        while k > 0:
            steps = countSteps(n, num)
            if steps <= k:
                # If the k-th number is not in the subtree rooted at 'num',
                # move to the next number.
                k -= steps
                num += 1
            else:
                # If the k-th number is in the subtree, go deeper
                num *= 10
                k -= 1
        
        return num


sol =Solution()

print(sol.findKthNumber(13,2))