from typing import List


class Solution:
    def maximumSumOfHeights(self, arr: List[int]) -> int:
        res = 0
        for i in range(len(arr)):
            curr, v = arr[i], arr[i]
            for j in range(i + 1, len(arr)):
                v = min(v, arr[j])
                curr += v

        v = arr[i]
        for j in range(i - 1, -1, -1):
            v = min(v, arr[j])
            curr +=v

        res = max(res, curr)

        return res
    

s= Solution()

sol = s.maximumSumOfHeights([5,3,4,1,1])
print(sol)