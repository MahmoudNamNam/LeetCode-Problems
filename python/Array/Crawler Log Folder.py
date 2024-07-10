from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cnt = 0
        for cmd in logs:
            if cmd == '../':
                if cnt > 0:
                    cnt -= 1
            elif cmd != './':
                cnt += 1
        return cnt
