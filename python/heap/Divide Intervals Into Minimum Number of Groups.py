import heapq
from typing import List

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        end_heap = []
        group_nums = 0

        for st, end in intervals:
            while end_heap and end_heap[0] < st:
                heapq.heappop(end_heap)
            heapq.heappush(end_heap, end)
            group_nums = max(group_nums, len(end_heap))

        return group_nums

    

sol  =Solution()
print(sol.minGroups(intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]))
print(sol.minGroups(intervals = [[1,3],[5,6],[8,10],[11,13]]))

