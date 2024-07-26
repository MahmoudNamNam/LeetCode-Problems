class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        try:
            return haystack.index(needle)
        except: return -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)