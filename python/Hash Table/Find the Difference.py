from typing import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = Counter(s)
        t_count = Counter(t)
        for char in t_count:
            if t_count[char] != s_count.get(char, 0):
                return char
        return ""