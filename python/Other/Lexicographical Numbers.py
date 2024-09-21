from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        num = 1
        for _ in range(n):
            result.append(num)
            if num * 10 <= n:
                num *= 10
            else:
                if num >= n:
                    num //= 10
                num += 1
                while num % 10 == 0:
                    num //= 10
        return result

sol =Solution()

print(sol.lexicalOrder(13))

'''
For n = 13:

Start with 1, then move to 10, 11, 12, 13.
Now, 14 exceeds n, so backtrack to 2, then 3, and so on.
Output: [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9].
'''