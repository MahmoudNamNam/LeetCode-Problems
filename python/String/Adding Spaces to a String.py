from typing import List
from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        spaces_set = set(spaces)
        for i in range(len(s)):
            if i in spaces_set:
                result.append(' ')
            result.append(s[i])
        return ''.join(result)

sol = Solution()
print(sol.addSpaces(s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]))
print(sol.addSpaces(s = "icodeinpython", spaces = [1,5,7,9]))