from typing import List
import datetime

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Convert time strings to minutes since midnight
        def timeToMinutes(time: str) -> int:
            hours, minutes = map(int, time.split(':'))
            return hours * 60 + minutes

        minutes = list(map(timeToMinutes, timePoints))
        minutes.sort()

        minutes.append(minutes[0] + 1440)

        # Calculate the minimum difference
        min_diff = min(minutes[i+1] - minutes[i] for i in range(len(minutes) - 1))
        
        return min_diff
