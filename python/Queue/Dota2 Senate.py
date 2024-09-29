from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        Radiant = deque()
        Dire = deque()
        for i in range(len(senate)):
            if senate[i]=='R':
                Radiant.append(i)
            else:
                Dire.append(i)
        while Radiant and Dire:
            r_idx = Radiant.popleft()
            d_idx = Dire.popleft()
            if r_idx < d_idx:  # Radiant acts first
                Radiant.append(r_idx + len(senate)) # Ban Dire and reinsert Radiant
            else:  # Dire acts first
                Dire.append(d_idx + len(senate))
        # Check which party has remaining senators
        return "Radiant" if Radiant else "Dire"
    

sol =Solution()

print(sol.predictPartyVictory(senate = "RD"))
print(sol.predictPartyVictory(senate = "RDD"))