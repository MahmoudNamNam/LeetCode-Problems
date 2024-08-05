from collections import Counter
from typing import List

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)
        
        distinct_strings = []
        
        for key, count in counter.items():
            if count == 1:
                distinct_strings.append(key)
        
        if k <= 0 or k > len(distinct_strings):
            return ""  
        
        return distinct_strings[k - 1]
