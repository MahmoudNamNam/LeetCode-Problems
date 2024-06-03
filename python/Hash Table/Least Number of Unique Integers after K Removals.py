from collections import Counter
from typing import List




class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # Step 1: Count the frequency of each integer in the array
        counter = Counter(arr)
        
        # Step 2: Sort the items based on their frequencies (in ascending order)
        freq_list = sorted(counter.items(), key=lambda item: item[1])
        
        # Step 3: Remove elements starting from the least frequent
        for key, count in freq_list:
            if k >= count:
                k -= count
                del counter[key]
            else:
                break
        
        # Step 4: The length of the remaining counter is the number of unique integers left
        return len(counter)


sol = Solution()
print(sol.findLeastNumOfUniqueInts(arr=[5, 5, 4], k=1))  # Output: 1
print(sol.findLeastNumOfUniqueInts(arr=[4, 3, 1, 1, 3, 3, 2], k=3))  # Output: 2
