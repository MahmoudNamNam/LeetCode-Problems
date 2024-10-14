from typing import Optional,List
import heapq,math

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        res =0
        max_heap=[-n for n in nums]
        heapq.heapify(max_heap)
        while k:
            n = -heapq.heappop(max_heap)
            res+=n
            k-=1
            heapq.heappush(max_heap,-math.ceil(n/3))

        return res

sol = Solution()
print(sol.maxKelements(nums = [10,10,10,10,10], k = 5))
print(sol.maxKelements(nums = [1,10,3,3,3], k = 3))