class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors=0
        for i in range(1,n+1):
            if n%i==0:
                factors+=1
            if factors==k:
                return i
        return -1

sol = Solution()
print(sol.kthFactor(n = 12, k = 3))


"""
Example 1:

Input: n = 12, k = 3
Output: 3
Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.
Example 2:

Input: n = 7, k = 2
Output: 7
Explanation: Factors list is [1, 7], the 2nd factor is 7.
Example 3:

Input: n = 4, k = 4
Output: -1
Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should return -1.

"""


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for i in range(1,n//2+1):
            if n%i==0:
                k-=1
            if k==0:
                return i
        if k==1:
            return n
        else:
            return -1