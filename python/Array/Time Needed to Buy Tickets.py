from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        cnt = 0

        for i in range(len(tickets)):
            if i <= k:
                cnt += min(tickets[i], tickets[k])
            else:
                cnt += min(tickets[i], tickets[k] - 1)

        return cnt

s = Solution()
print(s.timeRequiredToBuy([2,3,2],2))