from typing import Counter, List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        return len(cnt.values()) == len(set(cnt.values()))
        
sol = Solution()
arr = [1,2,2,1,1,3]
print(sol.uniqueOccurrences(arr))
arr = [1,2]
print(sol.uniqueOccurrences(arr))
arr = [-3,0,1,-3,1,1,1,-3,10,0]
print(sol.uniqueOccurrences(arr))
