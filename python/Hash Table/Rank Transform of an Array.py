from typing import List
from collections import Counter

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        return [sorted(arr).index(x) +1 for x in arr]
    




class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(set(arr))
        rank_map ={num:rank+1 for rank ,num in enumerate(sorted_arr)}
        print(arr)
        print(rank_map)
        return [rank_map[num] for num in arr]

sol = Solution()

arr = [37,12,28,9,100,56,80,5,5,12]
print(sol.arrayRankTransform(arr))




class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a={}
        rank=1
        for num in sorted(arr):
            if num not in a:
                a[num]=rank
                rank=rank+1
        return[a[i] for i in arr]

sol = Solution()

arr = [37,12,28,9,100,56,80,5,5,12]
print(sol.arrayRankTransform(arr))



