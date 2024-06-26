from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Find the shortest string in the array
        min_len = min(len(s) for s in strs)
        
        common_prefix = ""
        
        for i in range(min_len):
            current_char = strs[0][i]
            for string in strs:
                if string[i] != current_char:
                    return common_prefix
            common_prefix += current_char
        
        return common_prefix


sol =Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(sol.longestCommonPrefix(["dog", "racecar", "car"]))     # Output: ""
