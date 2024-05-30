class Solution:
    def numSplits(self, s: str) -> int:
        from collections import Counter
        
        if len(s) == 1 or len(s) ==0:  # never splittable
            return 0
        elif len(s) == 2:  # always splittable
            return 1
        left_counter = Counter()
        right_counter = Counter(s)
        
        good_splits = 0
        
        for char in s:
            left_counter[char] += 1
            right_counter[char] -= 1
            if right_counter[char] == 0:
                del right_counter[char]
            
            if len(left_counter) == len(right_counter):
                good_splits += 1
                
        return good_splits

    
sol =Solution()
print(sol.numSplits("aacaba")) #2
print(sol.numSplits("abcd")) #1
