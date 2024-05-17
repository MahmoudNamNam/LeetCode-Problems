from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        anagramMap = defaultdict(list)
        
        for word in strs:
            sortedWord = ''.join(sorted(word))
            anagramMap[sortedWord].append(word)
        
        return list(anagramMap.values())
    


strs = ["eat","tea","tan","ate","nat","bat"]

sol=Solution()

sol.groupAnagrams(strs)