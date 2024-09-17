from typing import Counter, List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s = (s1+' '+ s2).split(sep=' ')
        cnt = Counter(s)
        lst = []
        for key ,val in cnt.items():
            if val <2:
                lst.append(key)
        return lst

sol = Solution()
print(sol.uncommonFromSentences(s1 = "this apple is sweet", s2 = "this apple is sour"))
print(sol.uncommonFromSentences(s1 = "apple apple", s2 = "banana"))

