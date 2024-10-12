import heapq
from typing import List


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        for i in range(n):
            times[i].append(i)
        times.sort()
        available_chairs = []  # Min-heap for available chairs
        leaving_heap = []  # Min-heap for tracking when friends leave
        for i in range(n):
            heapq.heappush(available_chairs,i)
        
        # Simulate the party
        for arrival,leaving,friend_idx in times:
            # Before assigning a chair to the arriving friend, free up chairs of friends who have already left
            while leaving_heap and leaving_heap[0][0] <= arrival:
                _, chair = heapq.heappop(leaving_heap)
                heapq.heappush(available_chairs,chair)
            # Assign the smallest available chair to the arriving friend
            chair = heapq.heappop(available_chairs)

            if friend_idx == targetFriend:
                return chair
            
            # Add the friend to the leaving heap (so their chair becomes free when they leave)
            heapq.heappush(leaving_heap, (leaving, chair))


sol = Solution()
print(sol.smallestChair(times = [[1,4],[2,3],[4,6]], targetFriend = 2))
print(sol.smallestChair(times = [[3,10],[1,5],[2,6]], targetFriend = 0))
