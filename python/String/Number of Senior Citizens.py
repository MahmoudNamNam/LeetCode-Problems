from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt =0
        for passenger in details:
            if int(passenger[-4:-2])>60:
                cnt+=1
        return cnt


