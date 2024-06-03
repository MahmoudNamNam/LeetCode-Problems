class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        return len(t) - j

sol = Solution()
print(sol.appendCharacters(s = "coaching", t = "coding"))

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        lenT=len(t)
        for c in s:
            if c == t[i]:
                i += 1
                if i >=lenT:
                    return 0

        return lenT - i 