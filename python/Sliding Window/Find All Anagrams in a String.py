from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        p_count = Counter(p)
        window_len = len(p)
        right=window_len
        indices=[]
        window_count = Counter()
        for i in range(window_len):
            window_count[s[i]]+=1
        # Check the first window
        if window_count == p_count:
            indices.append(0)

        for i in range(window_len,len(s)):
            # Add the next character to the window
            window_count[s[i]] += 1
        
            # Remove the leftmost character from the window
            window_count[s[i - window_len]] -= 1
        
            # If the count becomes zero, remove it from the counter
            if window_count[s[i - window_len]] == 0:
                del window_count[s[i - window_len]]
            
            # Check if the current window matches p's character counts
            if window_count == p_count:
                indices.append(i - window_len + 1)
            right+=1
            

        return indices
sol = Solution()
print(sol.findAnagrams(s = "cbaebabacd", p = "abc"))