from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # Convert allowed string to a set for fast lookups
        allowed_set = set(allowed)
        
        consistent_count = 0
        
        for word in words:
            # Check if all characters in the word are in the allowed set
            if all(char in allowed_set for char in word):
                consistent_count += 1
        
        return consistent_count



class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        mySet=set(allowed)
        count=0
        for i in words:
            if set(i).issubset(mySet):
                count+=1
        return count