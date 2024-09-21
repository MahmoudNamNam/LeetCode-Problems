from typing import Counter, List


from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        freq = list(cnt.values()) 
        return len(freq) == len(set(freq))

        
sol = Solution()
arr = [1,2,2,1,1,3]
print(sol.uniqueOccurrences(arr))
arr = [1,2]
print(sol.uniqueOccurrences(arr))
arr = [-3,0,1,-3,1,1,1,-3,10,0]
print(sol.uniqueOccurrences(arr))
