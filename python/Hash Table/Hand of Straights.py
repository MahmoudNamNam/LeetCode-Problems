from typing import Counter, List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        card_count = Counter(hand)
        sorted_cards = sorted(card_count)
        
        for card in sorted_cards:
            while card_count[card] > 0:
                for i in range(groupSize):
                    if card_count[card + i] > 0:
                        card_count[card + i] -= 1
                    else:
                        return False
        return True
sol =Solution()


print(sol.isNStraightHand(hand = [1,2,3,6,2,3,4,7,8], groupSize = 3))

print(sol.isNStraightHand(hand = [1,2,3,4,5], groupSize = 4))