from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        zipped = zip(names, heights)
        sorted_zipped = sorted(zipped, key=lambda x: x[1])
        sorted_list1, _ = zip(*sorted_zipped)
        return sorted_list1


