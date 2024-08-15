from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        wallet_5 = 0
        wallet_10 = 0

        for i in bills:
            if i == 5:
                wallet_5 += 1
            elif i == 10:
                if wallet_5 < 1:
                    return False
                else:
                    wallet_10 += 1
                    wallet_5 -= 1
            elif i == 20:
                if wallet_10 > 0 and wallet_5 > 0:
                    wallet_10 -= 1
                    wallet_5 -= 1
                elif wallet_5 >= 3:
                    wallet_5 -= 3
                else:
                    return False

        return True
