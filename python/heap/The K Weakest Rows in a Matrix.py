import heapq
from typing import List
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        #  (number of soldiers, row index)
        soldier_count = [(sum(row), i) for i, row in enumerate(mat)]
        
        #  get the k smallest elements (weakest rows)
        k_weakest = heapq.nsmallest(k, soldier_count)
        
        # Extract the row indices from the tuples
        return [index for _, index in k_weakest]

sol = Solution()

print(sol.kWeakestRows( mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3))


