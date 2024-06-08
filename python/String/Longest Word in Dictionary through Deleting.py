from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def can_form_by_deleting(s, word):
            it = iter(s)
            return all(char in it for char in word)
            
        dictionary.sort(key=lambda x: (-len(x), x))
        
        for word in dictionary:
            if can_form_by_deleting(s, word):
                return word
        
        return ""


sol =Solution()
s = "abpcplea"
dictionary = ["ale","apple","monkey","plea"]
print(sol.findLongestWord(s,dictionary))

s = "abpcplea"
dictionary = ["a","b","c"]
print(sol.findLongestWord(s,dictionary))