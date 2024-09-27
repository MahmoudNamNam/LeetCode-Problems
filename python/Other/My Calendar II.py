from collections import defaultdict

class MyCalendarTwo:
    def __init__(self):
        # List to hold the booked intervals
        self.bookings = []
        
    def book(self, start: int, end: int) -> bool:
        # Check for overlaps with existing bookings
        for a, b in self.bookings:
            # Check if the new booking overlaps with the existing interval
            if start < b and end > a:
                # Calculate the overlapping sub-interval
                new_start = max(a, start)
                new_end = min(b, end)
                
                # Check if the sub-interval overlaps more than once
                if self.check(new_start, new_end):
                    return False  # Overlapping more than once, booking fails
        
        # If there are no conflicts, add the booking
        self.bookings.append((start, end))
        return True  # Booking successful
    
    def check(self, start: int, end: int) -> bool:
        overlap_count = 0
        
        for a, b in self.bookings:
            # Check for strict overlap
            if start < b and end > a:
                overlap_count += 1
                if overlap_count == 2:
                    return True  # Found more than one overlap
        
        return False  # No overlapping found

obj = MyCalendarTwo()
print(obj.book(10, 20))  # True
print(obj.book(50, 60))  # True
print(obj.book(10, 40))  # True
print(obj.book(5, 15))   # False
print(obj.book(5, 10))   # True
print(obj.book(25, 55))  # True


class MyCalendarTwo:
    def __init__(self):
        # List to hold single bookings
        self.bookings = []
        # List to hold overlapping intervals (double bookings)
        self.overlaps = []
        
    def book(self, start: int, end: int) -> bool:
        # First, check if the new booking overlaps with any existing double booking
        for a, b in self.overlaps:
            # Check if the new booking would cause a triple booking
            if start < b and end > a:
                return False  # Triple booking detected, reject the new booking
        
        # Check if the new booking would overlap with any existing single booking
        for a, b in self.bookings:
            # If it overlaps, calculate the overlapping sub-interval and add it to overlaps
            if start < b and end > a:
                new_start = max(a, start)
                new_end = min(b, end)
                self.overlaps.append((new_start, new_end))
        
        # Add the new booking to the list of single bookings
        self.bookings.append((start, end))
        return True  # Booking successful

# Test cases
obj = MyCalendarTwo()
print(obj.book(10, 20))  # True
print(obj.book(50, 60))  # True
print(obj.book(10, 40))  # True
print(obj.book(5, 15))   # False
print(obj.book(5, 10))   # True
print(obj.book(25, 55))  # True
