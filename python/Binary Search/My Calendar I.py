from bisect import bisect_left

class MyCalendar:

    def __init__(self):
        self.booked = []

    def book(self, start: int, end: int) -> bool:
        # Find the position to insert the new event using binary search
        i = bisect_left(self.booked, (start, end))
        
        # Check if there's a conflict with the previous event
        if i > 0 and self.booked[i-1][1] > start:
            return False  # Overlaps with the previous event

        # Check if there's a conflict with the next event
        if i < len(self.booked) and self.booked[i][0] < end:
            return False  # Overlaps with the next event

        # If no overlap, insert the new event into the list
        self.booked.insert(i, (start, end))
        return True

# Example usage:
obj = MyCalendar()
print(obj.book(10, 20))  # Should return True
print(obj.book(15, 25))  # Should return False (overlaps)
print(obj.book(20, 30))  # Should return True (no overlap)
